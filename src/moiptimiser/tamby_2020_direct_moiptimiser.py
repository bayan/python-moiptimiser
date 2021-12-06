from moiptimiser.tamby_2020_moiptimiser import *

class Tamby2020DirectMOIPtimiser(Tamby2020MOIPtimiser):

    def _delta_for_direct(self, k, u):
        delta = 1
        for i in range(self._model.NumObj):
            if i != k:
                delta = delta + u[i] - self._ideal_point[i]
        return delta

    def _construct_subproblem(self, k, u):
        # Direct Approach
        model = self._new_empty_objective_model()
        self._set_other_objectives_as_constraints(model, k, u)
        weights = [1] * self._model.NumObj
        weights[k] = self._delta_for_direct(k, u)
        summed_expression = self._summed_expression_from_objectives(model, weights)
        model.setObjective(summed_expression)
        model.update()
        self._find_and_set_start_values(model, k, u)
        return model
