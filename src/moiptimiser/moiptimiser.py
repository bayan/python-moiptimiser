import gurobipy

class MOIPtimiser:

    @classmethod
    def from_lp_file(cls, filepath):
        model = gurobipy.read(filepath)
        model.Params.OutputFlag = 0  # Suppress console output
        return cls(model)
