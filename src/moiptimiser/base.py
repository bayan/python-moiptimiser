import gurobipy as gp
from gurobipy import GRB

from moiptimiser.utilities import *

class MOIPtimiser:

    def __init__(self, model):
        self._model = model
        self._num_obj = model.NumObj
        self.num_solver_calls = 0
        self.num_infeasible = 0
        self._init_M()

    @classmethod
    def from_lp_file(cls, filepath):
        model = gp.read(filepath)
        model.Params.OutputFlag = 0  # Suppress console output
        return cls(model)

    def _init_M(self):
        self._M = GRB.MAXINT

    def _is_feasible(self, model):
        return model.getAttr('Status') == GRB.OPTIMAL

    def _is_infeasible(self, model):
        return not self._is_feasible(model)

    def _convert_to_min_problem(self):
        if self._model.ModelSense == GRB.MAXIMIZE:
            self._converted_from_max_problem = True
            self._model.ModelSense = GRB.MINIMIZE
            for i in range(self._num_obj):
                self._model.setObjectiveN(-self._model.getObjective(i), i, self._num_obj - i)
            self._model.update()
        else:
            self._converted_from_max_problem = False

    def strictly_dominates(self, left, right):
        return all((x < y for x, y in zip(left, right)))

    def weakly_dominates(self, left, right):
        return all((x <= y for x, y in zip(left, right)))

    def dominates(self, left, right):
        if left == right: return False
        return self.weakly_dominates(left, right)

    def _correct_sign_for_solution(self, solution):
        if self._converted_from_max_problem:
            return tuple([-x for x in solution])
        return solution

    def _correct_sign_for_solutions(self, solutions):
        if self._converted_from_max_problem:
            return set([self._correct_sign_for_solution(solution)
                        for solution in solutions])
        return solutions

    def _call_solver(self, model):
        self.num_solver_calls = self.num_solver_calls + 1
        model.optimize()
        if self._is_infeasible(model):
            self.num_infeasible = self.num_infeasible + 1

    def _copy_vars_to(self, source, target):
        for var in source.getVars():
            target.addVar(lb=var.lb, ub=var.ub, obj=var.obj,
                          vtype=var.vtype, name=var.VarName)
        target.update()

    def _copy_objective_to(self, source, target, sourceN, targetN, priority=0):
        source_objective = source.getObjective(sourceN)
        target_objective = gp.LinExpr()
        for i in range(source_objective.size()):
            var = source_objective.getVar(i)
            coeff = source_objective.getCoeff(i)
            new_var = target.getVarByName(var.VarName)
            target_objective.add(new_var, coeff)
        target.setObjectiveN(target_objective, targetN, priority)
        target.update()

    def _copy_constraints_to(self, source, target):
        for constr in source.getConstrs():
            constraint_expression = source.getRow(constr)
            new_expression = gp.LinExpr()
            for i in range(constraint_expression.size()):
                var = constraint_expression.getVar(i)
                coeff = constraint_expression.getCoeff(i)
                new_var = target.getVarByName(var.VarName)
                new_expression.add(new_var, coeff)
            target.addLConstr(new_expression, constr.Sense, constr.RHS, name=constr.ConstrName)
        target.update()

    def _new_empty_objective_model(self):
        new_model = gp.Model()
        new_model.Params.OutputFlag = 0  # Suppress console output
        self._copy_vars_to(self._model, new_model)
        self._copy_constraints_to(self._model, new_model)
        return new_model

    def _set_other_objectives_as_constraints(self, model, k, u, strict_inequality=True):
        constraints = []
        for i in range(self._num_obj):
            if i != k:
                other_objective = self._model.getObjective(i)
                new_expression = self._new_expression_from_objective(model, other_objective)
                rhs = u[i] - 0.5 if strict_inequality else u[i]
                constraint = model.addLConstr(new_expression, GRB.LESS_EQUAL, rhs)
                constraints.append(constraint)
        return constraints

    def _new_expression_from_objective(self, model, objective):
        new_expression = gp.LinExpr()
        for j in range(objective.size()):
            var = objective.getVar(j)
            coeff = objective.getCoeff(j)
            new_var = model.getVarByName(var.VarName)
            new_expression.add(new_var, coeff)
        return new_expression

    def _eval_linexpr_for_values(self, expression, vals_by_name):
        total = 0
        for i in range(expression.size()):
            var = expression.getVar(i)
            coeff = expression.getCoeff(i)
            value = vals_by_name[var.VarName]
            total = total + coeff * value
        return round(total)

    def _var_values_by_name_dict(self, model):
        vals_by_name = {}
        for var in model.getVars():
            vals_by_name[var.VarName] = var.X
        return vals_by_name

    def _eval_objective_given_model(self, model, objective):
        return self._eval_linexpr_for_values(objective, self._var_values_by_name_dict(model))
