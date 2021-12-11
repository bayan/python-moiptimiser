from moiptimiser.base import *
import itertools

class Tamby2020MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._convert_to_min_problem()
        self._defining_points = dict()
        self._decision_variable_map = dict()
        self._init_ideal_point()

    def _kth_projection(self, point, k):
        return tuple(list(point[0:k]) + list(point[k+1:len(point)]))

    # Algorithm 1
    def _update_search_region(self, new_point, search_region):
        # Output
        new_search_region = search_region.copy()
        # Line 2
        for u in search_region:
            # Line 3
            if self.strictly_dominates(new_point,u):
                # Line 4
                new_search_region.remove(u)
                # Line 5
                for l in range(self._num_obj):
                    # Line 6
                    ul = list(u)
                    ul[l] = new_point[l]
                    ul = tuple(ul)
                    # Line 7
                    for k in range(self._num_obj):
                        new_defining_points = set()
                        if k != l:
                            # Line 8
                            if (k,u) in self._defining_points:
                                for defining_point in self._defining_points[(k, u)]:
                                    if defining_point[l] < new_point[l]:
                                        new_defining_points.add(defining_point)
                        self._defining_points[(k, ul)] = new_defining_points
                    # Line 9
                    self._defining_points[(l,ul)] = set([new_point])
                    # Line 10
                    valid_defining_point_exists = True
                    for k in range(self._num_obj):
                        if k != l:
                            if ul[k] != self._M:
                                if len(self._defining_points[(k, ul)]) == 0:
                                    valid_defining_point_exists = False
                                    break
                    if valid_defining_point_exists:
                        # Line 11
                        new_search_region.add(ul)
            # Line 12
            else:
                for k in range(self._num_obj):
                    if new_point[k] == u[k]:
                        kth_new_point_projection = self._kth_projection(new_point, k)
                        kth_u_projection = self._kth_projection(u, k)
                        if self.strictly_dominates(kth_new_point_projection, kth_u_projection):
                            self._defining_points[(k,u)].add(new_point)
        return new_search_region

    def _set_start_values(self, model, values):
        for varname in values:
            model.getVarByName(varname).setAttr(GRB.Attr.Start, values[varname])

    def _kth_obj_model(self, k):
        new_model = self._new_empty_objective_model()
        self._copy_objective_to(self._model, new_model, k, 0)
        return new_model

    def _init_ideal_point(self):
        point = []
        for k in range(self._num_obj):
            kth_model = self._kth_obj_model(k)
            self._call_solver(kth_model)
            point.append(round(kth_model.ObjNVal))
        self._ideal_point = tuple(point)

    def _hypervolume_of_projection(self, k, u):
        h = 1
        for i in range(self._num_obj):
            if i != k:
                h = h * (u[i] - self._ideal_point[i])
        return h

    def _next_k_u(self, U):
        ku_pairs = list(itertools.product(range(self._num_obj), U))
        h_values = [ self._hypervolume_of_projection(k,u) for k,u in ku_pairs ]
        max_h = max(h_values)
        return ku_pairs[h_values.index(max_h)]

    def _find_and_set_start_values(self, model, k, u):
        if (k,u) in self._defining_points:
            N_ku = self._defining_points[(k,u)]
            if len(N_ku) > 0:
                feasible_nd = list(N_ku)[0]
                if feasible_nd in self._decision_variable_map:
                    feasible_variables = self._decision_variable_map[feasible_nd]
                    self._set_start_values(model, feasible_variables)

    def _summed_expression_from_objectives(self, model, weights):
        coefficient_dict = {}
        for i in range(self._num_obj):
            objective = self._model.getObjective(i)
            for j in range(objective.size()):
                var = objective.getVar(j)
                coeff = objective.getCoeff(j) * weights[i]
                if var.VarName not in coefficient_dict:
                    coefficient_dict[var.VarName] = 0
                coefficient_dict[var.VarName] = coefficient_dict[var.VarName] + coeff
        summed_expression = gp.LinExpr()
        for varname in coefficient_dict:
            new_var = model.getVarByName(varname)
            summed_expression.add(new_var, coefficient_dict[varname])
        return summed_expression

    def _upper_bounds_from_solved_model(self, model):
        upper_bounds = []
        for i in range(self._num_obj):
            upper_bounds.append(self._eval_objective_given_model(model, self._model.getObjective(i)))
        return tuple(upper_bounds)

    def _find_point(self, k, u):
        subproblem = self._construct_subproblem(k, u)
        self._call_solver(subproblem)
        new_point = tuple(
            [self._eval_objective_given_model(subproblem, self._model.getObjective(i))
             for i in range(self._num_obj)]
        )
        decision_variables = self._var_values_by_name_dict(subproblem)
        return (new_point, decision_variables)

    def _remove_dominated(self, nds):
        filtered = set()
        for nd in nds:
            if not any( (self.dominates(other, nd) for other in nds) ):
                filtered.add(nd)
        return filtered

    # Algorithm 2
    def find_non_dominated_objective_vectors(self):
        # Line 1
        N = set()
        U = set()
        U.add( tuple([self._M] * self._num_obj) )
        V = {}
        for k in range(self._num_obj):
            V[k] = set()

        # Line 2
        # Ideal point computed once already in the class constructor

        # Line 3
        while len(U) > 0:
            # Line 4
            k, u = self._next_k_u(U)
            # Line 5
            new_point, decision_variables = self._find_point(k, u)
            self._decision_variable_map[new_point] = decision_variables
            # Line 6
            V[k].add( (u, new_point[k]) )

            # Line 7
            if (k,u) not in self._defining_points:
                self._defining_points[(k,u)] = set()
            if new_point not in self._defining_points[(k,u)]:
                # Line 8
                U = self._update_search_region(new_point, U)
                # Line 9
                N.add(new_point)

            # Line 10
            for u_dash in U.copy():
                # Line 11
                for k in range(self._num_obj):
                    # Line 12
                    if u_dash[k] == self._ideal_point[k]:
                        # Line 13
                        U.remove(u_dash)
                    # Line 14
                    else:
                        # Line 15
                        for u, y_k in V[k]:
                            # Line 16
                            if y_k == u_dash[k] and u_dash in U:
                                kth_u_dash_projection = self._kth_projection(u_dash, k)
                                kth_u_projection = self._kth_projection(u, k)
                                weakly_dominated = self.weakly_dominates(kth_u_dash_projection, kth_u_projection)
                                if weakly_dominated:
                                    # Line 17
                                    U.remove(u_dash)
        # Line 18
        return self._correct_sign_for_solutions(self._remove_dominated(N))
