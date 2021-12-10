from moiptimiser.base import *

class Ozlen2014MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._convert_to_min_problem()

    def _nondominated_vector_for(self, bounds):
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


    def _find_non_dominated_objective_vectors(self, q, bounds=()):

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
                if new_vectors is None or len(new_vectors) == 0:
                    return N
                N = N.union(new_vectors)
                upper_bound = max([vector[q-1] for vector in new_vectors]) - 1


    def find_non_dominated_objective_vectors(self):
        N = self._find_non_dominated_objective_vectors(self._num_obj)
        return self._correct_sign_for_solutions(N)
