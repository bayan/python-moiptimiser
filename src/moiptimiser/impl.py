import gurobipy

class MOIPtimiser:

    def __init__(self, model):
        self.model = model

    def find_non_dominated_objective_vectors(self):
        self.model.optimize()
        solution = []
        for i in range(self.model.NumObj):
            self.model.params.ObjNumber = i
            solution.append(self.model.ObjNVal)
        return [tuple(solution)]

    def from_lp_file(filepath):
        model = gurobipy.read(filepath)
        model.Params.OutputFlag = 0 # Suppress console output
        return MOIPtimiser(model)
