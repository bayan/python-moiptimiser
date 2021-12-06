from moiptimiser.tamby_2020_moiptimiser import *

class Tamby2020TwoStageMOIPtimiser(Tamby2020MOIPtimiser):

    def _construct_subproblem(self, k, u):
        # Solve the first sub problem and return the second stage.

        # First stage
        stage1_model = self._kth_obj_model(k)
        self._set_other_objectives_as_constraints(stage1_model, k, u)
        self._find_and_set_start_values(stage1_model, k, u)
        self._call_solver(stage1_model)

        # Second stage
        stage2_model = self._new_empty_objective_model()
        upper_bounds = self._upper_bounds_from_solved_model(stage1_model)
        self._set_other_objectives_as_constraints(stage2_model, k, upper_bounds, strict_inequality=False)
        new_expression = self._new_expression_from_objective(self._model, self._model.getObjective(k))
        stage2_model.addLConstr(new_expression, GRB.EQUAL, round(stage1_model.ObjNVal))
        weights = [1] * self._model.NumObj
        summed_expression = self._summed_expression_from_objectives(stage2_model, weights)
        stage2_model.setObjective(summed_expression)
        self._set_start_values(stage2_model, self._var_values_by_name_dict(stage1_model))
        stage2_model.update()
        return stage2_model
