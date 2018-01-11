from copy import copy
from itertools import product


class Operator:

    def __init__(self, name, parameters, pre, add, del_, cost=1, constraints=None):
        self._name = name
        self._parameters = parameters
        self._pre = pre
        self._add = add
        self._del = del_
        self._cost = cost
        self._constraints = constraints or []

    def is_ground(self):
        return not any(map(lambda p: p[0][0] == "?", self._parameters))

    def ground(self, sigma):
        grop = copy(self)
        grop._parameters = [(sigma[p],t) for p,t in grop._parameters]
        grop._pre = substitute_parameter(grop._pre, sigma)
        grop._add = substitute_parameter(grop._add, sigma)
        grop._del = substitute_parameter(grop._del, sigma)
        return grop

    def __eq__(self, other):
        return self._name == other._name and self._parameters == other._parameters

    def ground_all(self, objects=None):
        ground_ops = []
        candidates = []
        for name, type_ in self._parameters:
            if type_ is None:
                params = objects
            else:
                params = filter(lambda t: type_ in t[1], objects)
            params = map(lambda p: p[0], params)
            candidates.append(list(params))
        for param_comb in product(*candidates):
            sigma = {p:o for o,(p,_) in zip(param_comb, self._parameters)}
            if all(map(lambda c: c(sigma), self._constraints)):
                ground_ops.append(self.ground(sigma))
        return ground_ops

    def name(self):
        return self._name

    def parameters(self):
        return self._parameters

    def cost(self):
        return self._cost

    def pre_list(self):
        return self._pre

    def add_list(self):
        return self._add

    def delete_list(self):
        return self._del

    def __str__(self):
        if self.is_ground():
            params = ",".join(map(lambda p: p[0], self._parameters))
        else:
            params = ",".join(map(lambda p: p[0]+"-"+p[1], self._parameters)) 
        return "{}({})".format(self._name, params)

    def verbose(self, indent=2):
        head = " "*indent + "- " + str(self) + ":"
        pre = " "*(indent+2) + "Pre: " + predicate_list_to_str(self._pre)
        add = " "*(indent+2) + "Add: " + predicate_list_to_str(self._add)
        del_ = " "*(indent+2) + "Delete: " + predicate_list_to_str(self._del)
        return "\n".join([head, pre, add, del_])


class State:

    def __init__(self, predicates, problem):
        self._predicates = frozenset(predicates)
        self._problem = problem
        self._hash = hash(self._predicates) # cache hash

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return self._predicates == other._predicates

    def problem(self):
        return self._problem

    def predicates(self):
        return self._predicates

    def satisfies(self, predicates):
        return self._predicates.issuperset(predicates)

    def entails(self, other):
        return self.satisfies(other._predicates)

    def difference(self, other):
        return self._predicates.difference(other._predicates)

    def can_apply(self, op):
        return self.satisfies(op.pre_list())

    def apply(self, op):
        new_state = None
        if self.can_apply(op):
            new_state = copy(self)
            predicates = new_state._predicates.union(op.add_list())
            predicates = predicates.difference(op.delete_list())
            new_state._predicates = predicates
        return new_state

    def __iter__(self):
        return self._predicates.__iter__()

    def __str__(self):
        return predicate_list_to_str(sorted(self._predicates))

    def _repr_svg_(self):
        problem = self._problem
        return self._problem.draw(self)

    def verbose(self, indent=2):
        return " "*indent + predicate_list_to_str(sorted(self._predicates), "\n"+" "*indent)


class Domain:

    def __init__(self, name, operators, predicates=None, types=None):
        self._name = name
        self._types = types or {}
        self._operators = operators
        self._predicates = predicates

    def name(self):
        return self._name

    def types(self):
        return self._types

    def operators(self):
        return self._operators

    def draw(self, problem, state):
        raise NotImplementedError()

    def generate_problem(self, *args, **kwargs):
        raise NotImplementedError()

    def __str__(self):
        operators = "\n".join(map(Operator.verbose, self._operators))
        return "Domain: {}\nTypes: {}\nOperators:\n{}".format(self._name,
                self._types, operators)


class Problem:

    def __init__(self, name, domain, objects, init, goal):
        self._name = name
        self._domain = domain
        self._objects = [(o,inferred_types(t, domain.types())) for o,t in objects]
        self._init = State(init, self) 
        self._goal = State(goal, self)
        self._operators = []
        for op in domain.operators():
            grops = op.ground_all(self._objects)
            self._operators += op.ground_all(self._objects)

    def name(self):
        return self._name

    def domain(self):
        return self._domain

    def objects(self):
        return self._objects

    def init(self):
        return self._init

    def goal(self):
        return self._goal

    def operators(self):
        return self._operators

    def draw(self, state):
        return self._domain.draw(self, state)

    def trivial(self):
        return self._init.entails(self._goal)

    def __str__(self):
        problem = "Problem: " + self._name
        domain = "Domain: " + self._domain.name()
        init = "Initial state:\n" + self._init.verbose()
        goal = "Goal:\n" + self._goal.verbose()
        operators = "Ground operators:\n  " + "\n  ".join(map(str, self._operators))
        return "\n".join([problem, domain, init, goal, operators])


def inferred_types(type_, hierarchy):
    types = []
    while type_ is not None:
        types.append(type_)
        type_ = hierarchy.get(type_, None)
    return types


def substitute_parameter(predicates, sigma):
    return [(pred[0],)+tuple(map(sigma.__getitem__, pred[1:])) for pred in predicates]


def predicate_list_to_str(predicates, delim=", "):
    return delim.join(map(lambda pred: pred[0]+"("+",".join(pred[1:])+")", predicates))


def all_different(sigma):
    different_values = set(sigma.values())
    return len(sigma) == len(different_values)


