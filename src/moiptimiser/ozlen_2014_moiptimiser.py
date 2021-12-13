from moiptimiser.base import *

class Ozlen2014MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._convert_to_min_problem()
        self._init_relaxation_cache()
        self._setup_objectives_as_constraints()

    def _init_relaxation_cache(self):
        self._relaxation_cache = {}
        for i in range(self._num_obj):
            self._relaxation_cache[i+1] = {}

    def _setup_objectives_as_constraints(self):
        bounds = tuple([self._M]*self._num_obj)
        self._objective_constraints = self._set_other_objectives_as_constraints(self._model, 0, bounds, strict_inequality=False)

    # Returns a tuple (N, infeasible).
    def _nondominated_vector_for(self, bounds):
        for i in range(self._num_obj - 1):
            self._objective_constraints[i].rhs = bounds[i]
        self._call_solver(self._model)
        if self._is_infeasible(self._model):
            return (None, True)
        return (self._current_nd(), False)

    def _current_nd(self):
        nd = []
        for i in range(self._num_obj):
            self._model.params.ObjNumber = i
            nd.append(round(self._model.ObjNVal))
        return tuple(nd)

    # Returns a tuple (N, infeasible).
    # N is the set of nondominated vectors found, and is None if none were found.
    # If N was found, but infeasible, then the second item in the returned tuple is True. It is False otherwise.
    def _find_relaxation(self, q, bounds):
        cache = self._relaxation_cache[q]
        for relaxation in cache:
            if self.weakly_dominates(bounds, relaxation):
                N = cache[relaxation]
                if N is None: return (None, True)
                if all( (self.weakly_dominates(vector[q:], bounds) for vector in N) ):
                    return (N, False)
        return (None, False)

    def _save_relaxation(self, q, bounds, N):
        self._relaxation_cache[q][bounds] = N

    def _find_non_dominated_objective_vectors(self, q, bounds=()):
        if q == 1:
            new_vector, infeasible = self._nondominated_vector_for(bounds)
            if infeasible: return None
            return { new_vector } # Return the vector within a set

        else:
            N = set()
            upper_bound = self._M
            while True:
                new_bounds = prepend_tuple(upper_bound, bounds)
                new_vectors, infeasible = self._find_relaxation(q-1, new_bounds)
                if infeasible:
                    return None if len(N) == 0 else N
                elif new_vectors is None:
                    new_vectors = self._find_non_dominated_objective_vectors(q-1, new_bounds)
                    self._save_relaxation(q-1, new_bounds, new_vectors)

                # At this point, we have looked up the relaxation cache and called the solver.
                if new_vectors is None:
                    return None if len(N) == 0 else N

                N = N.union(new_vectors)
                upper_bound = max([vector[q-1] for vector in new_vectors]) - 1

    def find_non_dominated_objective_vectors(self):
        N = self._find_non_dominated_objective_vectors(self._num_obj)
        return self._correct_sign_for_solutions(N)
