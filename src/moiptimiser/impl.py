import gurobipy

class MOIPtimiser:

    def __init__(self, model):
        self.__model = model
        self.__init_upper_bound_constraints()

    def __init_upper_bound_constraints(self):
        self.__objective_constraints = []
        for i in range(self.__model.NumObj):
            objective = self.__model.getObjective(i)
            constraint = self.__model.addConstr(objective, '<', gurobipy.GRB.INFINITY)
            self.__objective_constraints.append(constraint)

    def __is_feasible(self):
        return self.__model.getAttr('Status') == gurobipy.GRB.OPTIMAL

    def __is_infeasible(self):
        return not self.__is_feasible()

    def __current_nd(self):
        nd = []
        for i in range(self.__model.NumObj):
            self.__model.params.ObjNumber = i
            nd.append(int(self.__model.ObjNVal))
        return tuple(nd)

    def __find_non_dominated_objective_vectors(self, depth):
        if depth == 1:
            self.__model.optimize()
            if self.__is_infeasible():
                return []
            else:
                return [self.__current_nd()]
        else:
            nds = []
            self.__objective_constraints[-depth].rhs = gurobipy.GRB.INFINITY
            while True:
                new_nds = self.__find_non_dominated_objective_vectors(depth-1)
                if len(new_nds) == 0: return nds
                nds = nds + new_nds
                new_bound = max([ nd[depth-1] for nd in new_nds ]) - 1
                self.__objective_constraints[depth-1].rhs = new_bound

    def find_non_dominated_objective_vectors(self):
        return self.__find_non_dominated_objective_vectors(self.__model.NumObj)

    def from_lp_file(filepath):
        model = gurobipy.read(filepath)
        model.Params.OutputFlag = 0 # Suppress console output
        return MOIPtimiser(model)
