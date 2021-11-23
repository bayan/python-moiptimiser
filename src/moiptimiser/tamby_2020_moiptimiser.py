from moiptimiser.moiptimiser import *
import itertools

class Tamby2020MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)
        self._convert_to_min_problem()
        self._defining_points = dict()
        self._init_M()
        self._init_ideal_point()

    def _init_M(self):
        self._M = GRB.MAXINT

    def _kth_projection(self, point, k):
        return tuple(list(point[0:k]) + list(point[k+1:len(point)]))

    def strictly_dominates(self, left, right):
        return all((x < y for x, y in zip(left, right)))

    def weakly_dominates(self, left, right):
        return all((x <= y for x, y in zip(left, right)))

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
                for l in range(self._model.NumObj):
                    # Line 6
                    ul = list(u)
                    ul[l] = new_point[l]
                    ul = tuple(ul)
                    # Line 7
                    for k in range(self._model.NumObj):
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
                    if new_point[k] == u[k]:
                        kth_new_point_projection = self._kth_projection(new_point, k)
                        kth_u_projection = self._kth_projection(u, k)
                        if self.strictly_dominates(kth_new_point_projection, kth_u_projection):
                            self._defining_points[(k,u)].add(new_point)
        return new_search_region

    def _copy_vars_to(self, source, target):
        for var in source.getVars():
            target.addVar(lb=var.lb, ub=var.ub, obj=var.obj,
                          vtype=var.vtype, name=var.VarName)
        target.update()

    def _copy_objective_to(self, source, target, sourceN, targetN):
        source_objective = source.getObjective(sourceN)
        target_objective = gp.LinExpr()
        for i in range(source_objective.size()):
            var = source_objective.getVar(i)
            coeff = source_objective.getCoeff(i)
            new_var = target.getVarByName(var.VarName)
            target_objective.add(new_var, coeff)
        target.setObjectiveN(target_objective, targetN)
        target.update()

    def _copy_constraints_to(self, source, target):
        for constr in source.getConstrs():
            constraint_expression = source.getRow(constr)
            new_expression = gp.LinExpr()
            for i in range(constraint_expression.size()):
                var = constraint_expression.getVar(i)
                coeff = constraint_expression.getCoeff(i)
                new_var = target.getVarByName(var.VarName)
                new_expression.add(new_var, coeff)
            target.addLConstr(new_expression, constr.Sense, constr.RHS, name=constr.ConstrName)
        target.update()

    def _kth_obj_model(self, k):
        new_model = gp.Model(f"objective-{k}")
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
        return ku_pairs[h_values.index(max_h)]

    def _var_values_by_name_dict(self, model):
        vals_by_name = {}
        for var in model.getVars():
            vals_by_name[var.VarName] = var.X
        return vals_by_name

    def _eval_linexpr_for_values(self, expression, vals_by_name):
        total = 0
        for i in range(expression.size()):
            var = expression.getVar(i)
            coeff = expression.getCoeff(i)
            value = vals_by_name[var.VarName]
            total = total + coeff * value
        return int(total)

    def _eval_objective_given_model(self, model, objective):
        return self._eval_linexpr_for_values(objective, self._var_values_by_name_dict(model))

    def _construct_subproblem(self, k, u):
        # For the Two-Stage Approach, solve the first sub problem and return the second stage.
        # For the Direct Approach, return the weighted single objective problem.
        # First, we implement the Two-Stage Approach.

        # First stage
        stage1_model = self._kth_obj_model(k)
        for i in range(self._model.NumObj):
            if i != k:
                other_objective = self._model.getObjective(i)
                new_expression = gp.LinExpr()
                for j in range(other_objective.size()):
                    var = other_objective.getVar(j)
                    coeff = other_objective.getCoeff(j)
                    new_var = stage1_model.getVarByName(var.VarName)
                    new_expression.add(new_var, coeff)
                # Alter u[i] because Gurobi does not support strict < inequality
                stage1_model.addLConstr(new_expression, GRB.LESS_EQUAL, u[i] - 0.5)
        stage1_model.optimize()

        # Second stage
        stage2_model = gp.Model()
        stage2_model.Params.OutputFlag = 0  # Suppress console output
        self._copy_vars_to(self._model, stage2_model)
        self._copy_constraints_to(self._model, stage2_model)

        coefficient_dict = {}
        for i in range(self._model.NumObj):
            other_objective = self._model.getObjective(i)
            new_expression = gp.LinExpr()
            for j in range(other_objective.size()):
                var = other_objective.getVar(j)
                coeff = other_objective.getCoeff(j)
                new_var = stage1_model.getVarByName(var.VarName)
                new_expression.add(new_var, coeff)
                if i != k:
                    if var.VarName not in coefficient_dict:
                        coefficient_dict[var.VarName] = 0
                    coefficient_dict[var.VarName] = coefficient_dict[var.VarName] + coeff
            if i == k:
                rhs = int(stage1_model.ObjNVal)
                constraint_sense = GRB.EQUAL
            else:
                rhs = self._eval_objective_given_model(stage1_model, self._model.getObjective(i))
                constraint_sense = GRB.LESS_EQUAL
            stage2_model.addLConstr(new_expression, constraint_sense, rhs)

        # Set the objective for the stage 2 model
        summed_expression = gp.LinExpr()
        for varname in coefficient_dict:
            new_var = stage2_model.getVarByName(varname)
            summed_expression.add(new_var, coefficient_dict[varname])
        stage2_model.setObjective(summed_expression)
        stage2_model.update()
        return stage2_model

    def _find_point(self, k, u):
        subproblem = self._construct_subproblem(k, u)
        subproblem.optimize()
        new_point = tuple(
            [self._eval_objective_given_model(subproblem, self._model.getObjective(i))
             for i in range(self._model.NumObj)]
        )
        return new_point

    # Algorithm 2
    def find_non_dominated_objective_vectors(self):
        # Line 1
        N = set()
        U = set()
        U.add( tuple([self._M] * self._model.NumObj) )
        V = {}
        for k in range(self._model.NumObj):
            V[k] = set()

        # Line 2
        # Ideal point computed once already in the class constructor

        # Line 3
        while len(U) > 0:
            # Line 4
            k, u = self._next_k_u(U)
            # Line 5 - but without specifying a starting solution for now
            new_point = self._find_point(k, u)
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
                for k in range(self._model.NumObj):
                    # Line 12
                    if u_dash[k] == self._ideal_point[k]:
                        # Line 13
                        U.remove(u_dash)
                    # Line 14
                    else:
                        # Line 15
                        for u, y_k in V[(k)]:
                            # Line 16
                            if u_dash in U:
                                kth_u_dash_projection = self._kth_projection(u_dash, k)
                                kth_u_projection = self._kth_projection(u, k)
                                weakly_dominated = self.weakly_dominates(kth_u_dash_projection, kth_u_projection)
                                if weakly_dominated and y_k == u_dash[k]:
                                    # Line 17
                                    U.remove(u_dash)
        # Line 18
        return self._correct_sign_for_solutions(N)
