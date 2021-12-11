from moiptimiser.base import *

class Ozlen2014MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._convert_to_min_problem()
        self._init_relaxation_cache()
        self._nd_counter = 0

    def _init_relaxation_cache(self):
        self._relaxation_cache = {}
        for i in range(self._num_obj):
            self._relaxation_cache[i+1] = {}

    def _nondominated_vector_for(self, bounds):
        self._nd_counter = self._nd_counter + 1
        model = self._new_empty_objective_model()
        constraints = self._set_other_objectives_as_constraints(model, 0, prepend_tuple(self._M, bounds), strict_inequality=False)
        for i in range(self._num_obj):
            if i > 0:
                model.remove(constraints[i-1])
            self._copy_objective_to(self._model, model, i, 0)
            self._call_solver(model)
            if self._is_infeasible(model):
                return None
            upper_bound = round(self._eval_objective_given_model(model, self._model.getObjective(i)))
            new_expression = self._new_expression_from_objective(self._model, self._model.getObjective(i))
            model.addLConstr(new_expression, GRB.EQUAL, upper_bound)
        vector = [ self._eval_objective_given_model(model, self._model.getObjective(i))
                   for i in range(self._num_obj) ]
        return tuple(vector)


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
        N, infeasible = self._find_relaxation(q, bounds)
        if infeasible: return None
        if N is not None: return N

        if q == 1:
            new_vector = self._nondominated_vector_for(bounds)
            N = new_vector and {new_vector} # Returns None if it was infeasible
            return N

        else:
            N = set()
            upper_bound = self._M
            while True:
                new_bounds = prepend_tuple(upper_bound, bounds)
                new_vectors = self._find_non_dominated_objective_vectors(q-1, new_bounds)
                self._save_relaxation(q-1, new_bounds, new_vectors)
                if new_vectors is None:
                    return None if len(N) == 0 else N
                N = N.union(new_vectors)
                upper_bound = max([vector[q-1] for vector in new_vectors]) - 1


    def find_non_dominated_objective_vectors(self):
        N = self._find_non_dominated_objective_vectors(self._num_obj)
        return self._correct_sign_for_solutions(N)
