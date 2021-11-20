from moiptimiser.moiptimiser import *

class Tamby2020MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._init_ideal_point()

    def _update_search_region(self):
        pass

    def _find_non_dominated_objective_vectors(self):
        nds = set()
        return nds

    def _copy_vars_to(self, source, target):
        for var in source.getVars():
            target.addVar(lb=var.lb, ub=var.ub, obj=var.obj,
                          vtype=var.vtype, name=var.varname)
        target.update()

    def _copy_objective_to(self, source, target, sourceN, targetN):
        source_objective = source.getObjective(sourceN)
        target_objective = gurobipy.LinExpr()
        for i in range(source_objective.size()):
            var = source_objective.getVar(i)
            coeff = source_objective.getCoeff(i)
            new_var = target.getVarByName(var.Varname)
            target_objective.add(new_var, coeff)
        target.setObjectiveN(target_objective, targetN)
        target.update()

    def _copy_constraints_to(self, source, target):
        for constr in source.getConstrs():
            constraint_expression = source.getRow(constr)
            new_expression = gurobipy.LinExpr()
            for i in range(constraint_expression.size()):
                var = constraint_expression.getVar(i)
                coeff = constraint_expression.getCoeff(i)
                new_var = target.getVarByName(var.Varname)
                new_expression.add(new_var, coeff)
            target.addConstr(new_expression, constr.Sense, constr.RHS, name=constr.ConstrName)
        target.update()


    def _kth_obj_model(self, k):
        new_model = gurobipy.Model(f"objective-{k}")
        self._copy_vars_to(self._model, new_model)
        self._copy_objective_to(self._model, new_model, k, 0)
        self._copy_constraints_to(self._model, new_model)
        return new_model

    def _init_ideal_point(self):
        point = []
        for k in range(self._model.NumObj):
            kth_model = self._kth_obj_model(k)
            kth_model.optimize()
            point.append(kth_model.ObjNVal)
        self._ideal_point = tuple(point)
    def find_non_dominated_objective_vectors(self):
        nds = self._find_non_dominated_objective_vectors()
        return nds
