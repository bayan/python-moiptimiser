import gurobipy as gp
from gurobipy import GRB

from moiptimiser.utilities import *

class MOIPtimiser:

    def __init__(self, model):
        self._model = model
        self.num_solver_calls = 0
        self.num_infeasible = 0

    @classmethod
    def from_lp_file(cls, filepath):
        model = gp.read(filepath)
        model.Params.OutputFlag = 0  # Suppress console output
        return cls(model)

    def _is_feasible(self, model=None):
        if model is None:
            model = self._model
        return model.getAttr('Status') == GRB.OPTIMAL

    def _is_infeasible(self, model=None):
        return not self._is_feasible(model)

    def _convert_to_min_problem(self):
        if self._model.ModelSense == GRB.MAXIMIZE:
            self._converted_from_max_problem = True
            self._model.ModelSense = GRB.MINIMIZE
            for i in range(self._model.NumObj):
                self._model.setObjectiveN(-self._model.getObjective(i), i)
            self._model.update()
        else:
            self._converted_from_max_problem = False

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
