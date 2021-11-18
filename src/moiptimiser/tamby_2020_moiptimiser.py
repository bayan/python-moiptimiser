import gurobipy
from moiptimiser.moiptimiser import MOIPtimiser

class Tamby2020MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        self.__model = model
        self.__init_bound_constraints()

    def __init_bound_constraints(self):
        self.__objective_constraints = []
        for i in range(self.__model.NumObj):
            objective = self.__model.getObjective(i)
            if self.__is_min():
                constraint = self.__model.addLConstr(objective, '<', gurobipy.GRB.INFINITY)
            else:
                constraint = self.__model.addLConstr(objective, '>', -gurobipy.GRB.INFINITY)
            self.__objective_constraints.append(constraint)

    def __is_min(self):
        return self.__model.ModelSense == 1

    def __update_search_region(self):
        pass

    def __find_non_dominated_objective_vectors(self):
        nds = set()
        return nds

    def find_non_dominated_objective_vectors(self):
        nds = self.__find_non_dominated_objective_vectors()
        return nds
