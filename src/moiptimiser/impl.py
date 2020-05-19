import gurobipy


class MOIPtimiser:

    def __init__(self, model):
        self.__model = model
        self.__init_upper_bound_constraints()
        self.__relaxation_cache = {}

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

    def __current_bounds(self):
        bounds = []
        for i in range(self.__model.NumObj):
            bounds.append(self.__objective_constraints[i].rhs)
        return tuple(bounds)

    def __store_relaxation_in_cache(self, depth, bounds, solutions):
        if depth not in self.__relaxation_cache:
            self.__relaxation_cache[depth] = {}
        self.__relaxation_cache[depth][bounds] = solutions

    def __find_feasible_relaxation(self, depth):
        relaxations_at_depth = self.__relaxation_cache.get(depth)
        if relaxations_at_depth is not None:
            bounds = self.__current_bounds()
            for other_bounds in relaxations_at_depth:
                if bounds[depth:] != other_bounds and all((x >= y for x, y in zip(other_bounds, bounds[depth:]))):
                    is_feasible = True
                    nds = relaxations_at_depth[other_bounds]
                    for solution in nds:
                        if not all((x >= y for x, y in zip(bounds[depth:], solution[depth:]))):
                            is_feasible = False
                            break
                    if is_feasible:
                        return nds

    def __find_non_dominated_objective_vectors(self, depth):
        relaxation = self.__find_feasible_relaxation(depth)
        if relaxation is not None:
            return relaxation

        elif depth == 1:
            self.__model.optimize()
            nds = set() if self.__is_infeasible() else {self.__current_nd()}
            self.__store_relaxation_in_cache(depth, self.__current_bounds()[depth:], nds)
            return nds

        else:
            nds = set()
            new_bound = gurobipy.GRB.INFINITY
            while True:
                self.__objective_constraints[depth-1].rhs = new_bound
                self.__model.update()
                new_nds = self.__find_non_dominated_objective_vectors(depth-1)
                if len(new_nds) == 0:
                    self.__store_relaxation_in_cache(depth, self.__current_bounds()[depth:], nds)
                    return nds
                nds = nds.union(new_nds)
                new_bound = max([nd[depth-1] for nd in new_nds]) - 1

    def find_non_dominated_objective_vectors(self):
        nds = self.__find_non_dominated_objective_vectors(self.__model.NumObj)
        return nds

    def from_lp_file(filepath):
        model = gurobipy.read(filepath)
        model.Params.OutputFlag = 0  # Suppress console output
        return MOIPtimiser(model)
