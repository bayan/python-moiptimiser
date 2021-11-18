import gurobipy

class MOIPtimiser:

    def __init__(self, model):
        self._model = model
        self._init_bound_constraints()

    def _init_bound_constraints(self):
        self._objective_constraints = []
        for i in range(self._model.NumObj):
            objective = self._model.getObjective(i)
            if self._is_min():
                constraint = self._model.addLConstr(objective, '<', gurobipy.GRB.INFINITY)
            else:
                constraint = self._model.addLConstr(objective, '>', -gurobipy.GRB.INFINITY)
            self._objective_constraints.append(constraint)

    def _is_min(self):
        return self._model.ModelSense == 1

    @classmethod
    def from_lp_file(cls, filepath):
        model = gurobipy.read(filepath)
        model.Params.OutputFlag = 0  # Suppress console output
        return cls(model)
