import gurobipy as gp
from gurobipy import GRB

from moiptimiser.utilities import *

class MOIPtimiser:

    def __init__(self, model):
        self._model = model

    @classmethod
    def from_lp_file(cls, filepath):
        model = gp.read(filepath)
        model.Params.OutputFlag = 0  # Suppress console output
        return cls(model)

    def _is_min(self):
        return self._model.ModelSense == GRB.MINIMIZE

    def _is_max(self):
        return not self._is_min()

    def _convert_to_min_problem(self):
        if self._is_max():
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
