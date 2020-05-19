import gurobipy


class MOIPtimiser:

    def __init__(self, model):
        self.__model = model
        self.__init_bound_constraints()
        self.__relaxation_cache = {}

    def __init_bound_constraints(self):
        self.__objective_constraints = []
        for i in range(self.__model.NumObj):
            objective = self.__model.getObjective(i)
            if self.__is_min():
                constraint = self.__model.addConstr(objective, '<', gurobipy.GRB.INFINITY)
            else:
                constraint = self.__model.addConstr(objective, '>', -gurobipy.GRB.INFINITY)
            self.__objective_constraints.append(constraint)

    def __is_min(self):
        return self.__model.ModelSense == 1

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

    # True if each left[i] >= right[i]
    def __all_ge(self, left, right):
        return all((x >= y for x, y in zip(left, right)))

    # True if each left[i] <= right[i]
    def __all_le(self, left, right):
        return all((x <= y for x, y in zip(left, right)))

    # True if left is relaxation of the right
    def __is_relaxation(self, left, right):
        if self.__is_min():
            return right != left and self.__all_ge(left, right)
        else:
            return right != left and self.__all_le(left, right)

    def __are_feasible_vectors_at_depth(self, bounds, vectors, depth):
        for solution in vectors:
            if self.__is_min() and not self.__all_ge(bounds[depth:], solution[depth:]):
                return False
            if not self.__is_min() and not self.__all_le(bounds[depth:], solution[depth:]):
                return False
        return True

    def __find_feasible_relaxation(self, depth):
        relaxations_at_depth = self.__relaxation_cache.get(depth)
        if relaxations_at_depth is not None:
            bounds = self.__current_bounds()
            for other_bounds in relaxations_at_depth:
                if self.__is_relaxation(other_bounds, bounds[depth:]):
                    nds = relaxations_at_depth[other_bounds]
                    if self.__are_feasible_vectors_at_depth(bounds, nds, depth):
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
            new_bound = gurobipy.GRB.INFINITY if self.__is_min() else -gurobipy.GRB.INFINITY
            while True:
                self.__objective_constraints[depth-1].rhs = new_bound
                self.__model.update()
                new_nds = self.__find_non_dominated_objective_vectors(depth-1)
                if len(new_nds) == 0:
                    self.__store_relaxation_in_cache(depth, self.__current_bounds()[depth:], nds)
                    return nds
                nds = nds.union(new_nds)
                if self.__is_min():
                    new_bound = max([nd[depth-1] for nd in new_nds]) - 1
                else:
                    new_bound = min([nd[depth-1] for nd in new_nds]) + 1

    def find_non_dominated_objective_vectors(self):
        nds = self.__find_non_dominated_objective_vectors(self.__model.NumObj)
        return nds

    def from_lp_file(filepath):
        model = gurobipy.read(filepath)
        model.Params.OutputFlag = 0  # Suppress console output
        return MOIPtimiser(model)
