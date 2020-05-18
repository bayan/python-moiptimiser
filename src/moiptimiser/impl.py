import gurobipy

class MOIPtimiser:

    def __init__(self, model):
        self.model = model

    def find_non_dominated_objective_vectors(self):
        return [(50,24),(39,28),(34,29),(31,30),(30,31),(27,36),(24,45),(23,46),(21,55)]

    def from_lp_file(filepath):
        model = gurobipy.read(filepath)
        return MOIPtimiser(model)
