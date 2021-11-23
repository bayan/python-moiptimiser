from moiptimiser.moiptimiser import *

class Ozlen2014MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._init_bound_constraints()
        self._relaxation_cache = {}

    def _init_bound_constraints(self):
        self._objective_constraints = []
        for i in range(self._model.NumObj):
            objective = self._model.getObjective(i)
            if self._is_min():
                constraint = self._model.addLConstr(objective, '<', GRB.INFINITY)
            else:
                constraint = self._model.addLConstr(objective, '>', -GRB.INFINITY)
            self._objective_constraints.append(constraint)

    def _is_feasible(self):
        return self._model.getAttr('Status') == GRB.OPTIMAL

    def _is_infeasible(self):
        return not self._is_feasible()

    def _current_nd(self):
        nd = []
        for i in range(self._model.NumObj):
            self._model.params.ObjNumber = i
            nd.append(int(self._model.ObjNVal))
        return tuple(nd)

    def _current_bounds(self):
        bounds = []
        for i in range(self._model.NumObj):
            bounds.append(self._objective_constraints[i].rhs)
        return tuple(bounds)

    def _store_relaxation_in_cache(self, depth, bounds, solutions):
        if depth not in self._relaxation_cache:
            self._relaxation_cache[depth] = {}
        self._relaxation_cache[depth][bounds] = solutions

    # True if each left[i] >= right[i]
    def _all_ge(self, left, right):
        return all((x >= y for x, y in zip(left, right)))

    # True if each left[i] <= right[i]
    def _all_le(self, left, right):
        return all((x <= y for x, y in zip(left, right)))

    # True if left is relaxation of the right
    def _is_relaxation(self, left, right):
        if self._is_min():
            return right != left and self._all_ge(left, right)
        else:
            return right != left and self._all_le(left, right)

    def _are_feasible_vectors_at_depth(self, bounds, vectors, depth):
        for solution in vectors:
            if self._is_min() and not self._all_ge(bounds[depth:], solution[depth:]):
                return False
            if self._is_max() and not self._all_le(bounds[depth:], solution[depth:]):
                return False
        return True

    def _find_feasible_relaxation(self, depth):
        relaxations_at_depth = self._relaxation_cache.get(depth)
        if relaxations_at_depth is not None:
            bounds = self._current_bounds()
            for other_bounds in relaxations_at_depth:
                if self._is_relaxation(other_bounds, bounds[depth:]):
                    nds = relaxations_at_depth[other_bounds]
                    if self._are_feasible_vectors_at_depth(bounds, nds, depth):
                        return nds

    def _find_non_dominated_objective_vectors(self, depth):
        relaxation = self._find_feasible_relaxation(depth)
        if relaxation is not None:
            return relaxation

        elif depth == 1:
            self._model.optimize()
            nds = set() if self._is_infeasible() else {self._current_nd()}
            self._store_relaxation_in_cache(depth, self._current_bounds()[depth:], nds)
            return nds

        else:
            nds = set()
            new_bound = GRB.INFINITY if self._is_min() else -GRB.INFINITY
            while True:
                self._objective_constraints[depth-1].rhs = new_bound
                self._model.update()
                new_nds = self._find_non_dominated_objective_vectors(depth-1)
                if len(new_nds) == 0:
                    self._store_relaxation_in_cache(depth, self._current_bounds()[depth:], nds)
                    return nds
                nds = nds.union(new_nds)
                if self._is_min():
                    new_bound = max([nd[depth-1] for nd in new_nds]) - 1
                else:
                    new_bound = min([nd[depth-1] for nd in new_nds]) + 1

    def find_non_dominated_objective_vectors(self):
        nds = self._find_non_dominated_objective_vectors(self._model.NumObj)
        return nds
