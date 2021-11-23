import gurobipy as gp
from gurobipy import GRB

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
