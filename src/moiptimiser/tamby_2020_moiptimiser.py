from moiptimiser.moiptimiser import *
import itertools

class Tamby2020MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._search_region = set()
        self._defining_points = dict()
        self._init_M()
        self._init_ideal_point()

    def _init_M(self):
        self._M = gurobipy.GRB.MAXINT

    def _kth_projection(self, point, k):
        return tuple(list(point[0:k]) + list(point[k+1:len(point)]))

    def strictly_dominates(self, left, right):
        return all((x < y for x, y in zip(left, right)))

    # Algorithm 1
    def _update_search_region(self, new_point):
        # Output
        new_search_region = self._search_region.copy()
        # Line 2
        for u in self._search_region:
            # Line 3
            if self.strictly_dominates(new_point,u):
                # Line 4
                new_search_region.remove(u)
                # Line 5
                for l in range(self._model.NumObj):
                    # Line 6
                    ul = u.copy()
                    ul[l] = new_point[l]
                    ul = tuple(ul)
                    # Line 7
                    for k in range(self._model.NumObj):
                        new_defining_points = set()
                        if k != l:
                            # Line 8
                            for defining_point in self._defining_points[(k, u)]:
                                if defining_point[l] < new_point[l]:
                                    new_defining_points.add(defining_point)
                        self._defining_points[(k, ul)] = new_defining_points
                    # Line 9
                    self._defining_points[(l,ul)] = set([new_point])
                    # Line 10
                    valid_defining_point_exists = True
                    for k in range(self._model.NumObj):
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
                for k in range(self._model.NumObj):
                    if k != l:
                        if new_point[k] == u[k]:
                            kth_new_point_projection = self._kth_projection(new_point, k)
                            kth_u_projection = self._kth_projection(u, k)
                            if self.strictly_dominates(kth_new_point_projection, kth_u_projection):
                                self._defining_points[(k,u)].add(new_point)

    def _copy_vars_to(self, source, target):
        for var in source.getVars():
            target.addVar(lb=var.lb, ub=var.ub, obj=var.obj,
                          vtype=var.vtype, name=var.varname)
        target.update()

    def _copy_objective_to(self, source, target, sourceN, targetN):
        source_objective = source.getObjective(sourceN)
        target_objective = gurobipy.LinExpr()
        for i in range(source_objective.size()):
            var = source_objective.getVar(i)
            coeff = source_objective.getCoeff(i)
            new_var = target.getVarByName(var.Varname)
            target_objective.add(new_var, coeff)
        target.setObjectiveN(target_objective, targetN)
        target.update()

    def _copy_constraints_to(self, source, target):
        for constr in source.getConstrs():
            constraint_expression = source.getRow(constr)
            new_expression = gurobipy.LinExpr()
            for i in range(constraint_expression.size()):
                var = constraint_expression.getVar(i)
                coeff = constraint_expression.getCoeff(i)
                new_var = target.getVarByName(var.Varname)
                new_expression.add(new_var, coeff)
            target.addLConstr(new_expression, constr.Sense, constr.RHS, name=constr.ConstrName)
        target.update()

    def _kth_obj_model(self, k):
        new_model = gurobipy.Model(f"objective-{k}")
        new_model.Params.OutputFlag = 0  # Suppress console output
        self._copy_vars_to(self._model, new_model)
        self._copy_objective_to(self._model, new_model, k, 0)
        self._copy_constraints_to(self._model, new_model)
        return new_model

    def _init_ideal_point(self):
        point = []
        for k in range(self._model.NumObj):
            kth_model = self._kth_obj_model(k)
            kth_model.optimize()
            point.append(int(kth_model.ObjNVal))
        self._ideal_point = tuple(point)

    def _hypervolume_of_projection(self, k, u):
        h = 1
        for i in range(self._model.NumObj):
            if i != k:
                h = h * (u[i] - self._ideal_point[i])
        return h

    def _next_k_u(self, U):
        ku_pairs = list(itertools.product(range(self._model.NumObj), U))
        h_values = [ self._hypervolume_of_projection(k,u) for k,u in ku_pairs ]
        max_h = max(h_values)
        return h_values[h_values.index(max_h)]

    # Algorithm 2
    def find_non_dominated_objective_vectors(self):
        # Output
        Y_ND = set()

        # Line 1
        N = set()
        U = set([self._M] * self._model.NumObj)
        V = {}
        for k in range(self._model.NumObj):
            V[k] = set()

        # Line 2
        # Ideal point already computed on class instantiation.

        # Line 3
        while len(U) > 0:

            # Line 4
            k, u = self._next_k_u(U)

        # Output
        return Y_ND
