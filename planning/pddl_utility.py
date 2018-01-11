import os

from tempfile import NamedTemporaryFile
from copy import deepcopy
from math import log


def obj_to_str(obj):
    if isinstance(obj, (list, tuple)):
        return '{} - {}'.format(obj[0], obj[1])
    else:
        return obj


def predicate_to_str(predicate, positive=True):
    if len(predicate) == 1:
        # 0-arity simple predicate
        ret = "({})".format(predicate[0])
    else:
        # n-ary (n>0) simple predicate
        ret = "({} {})".format(predicate[0], " ".join(map(obj_to_str, predicate[1:])))
    if not positive:
        ret = "(not " + ret + ")"
    return ret


def predicate_list_to_str(predicates):
    return '\n'.join(map(predicate_to_str, predicates))


def pddl_hierarchy(types):
    return '\n'.join(["{} - {}".format(entry[0], entry[1])
                     for entry in types.items()])


pddl_action_template = """
(:action {action_name}
:parameters ({parameters})
:precondition (and {precondition})
:effect (and {effect} (increase (total-cost) {cost}))
)
"""

def pddl_action(op):
    parameters = "" if op.is_ground() else " ".join(map(obj_to_str, op.parameters()))
    cost = op.cost()
    pre = " ".join(map(predicate_to_str, op.pre_list()))
    effect = " ".join(map(predicate_to_str, op.add_list())) + " " +\
            " ".join(map(lambda p: predicate_to_str(p, False), op.delete_list()))
    name = op.name()
    if op.is_ground() and op.parameters():
        name += "__" + "__".join(map(lambda p: p[0], op.parameters()))
    pddl = pddl_action_template.format(
            action_name=name,
            parameters=parameters,
            precondition=pre,
            effect=effect,
            cost=cost
    )
    return pddl

def pddl_actions(ops):
    action_l = (pddl_action(op) for op in ops)
    return "\n\n".join(action_l)


pddl_domain_template = """
(define (domain {domain_name})
(:requirements :strips :typing :action-costs)
(:types
{types})
(:predicates
{predicate_specification})
(:functions (total-cost) - number)
{actions})
"""

def pddl_domain(domain, ops=None):
    ops = ops or domain.operators()
    pddl = pddl_domain_template.format(
            domain_name=domain.name(),
            types=pddl_hierarchy(domain.types()),
            predicate_specification=predicate_list_to_str(domain.predicates()),
            actions=pddl_actions(ops)
    )
    return pddl


pddl_problem_template = """
(define (problem {problem_name})
(:domain {domain_name})
(:objects {object_list})
(:init
(= (total-cost) 0)
{init_state})
(:goal (and {goal_condition}))
(:metric minimize (total-cost)))
"""

def pddl_problem(problem):
    object_list = []
    pddl = pddl_problem_template.format(
            problem_name=problem.name(),
            domain_name=problem.domain().name(),
            object_list=' '.join(map(obj_to_str, problem.objects())),
            init_state=predicate_list_to_str(list(problem.init().predicates())),
            goal_condition=predicate_list_to_str(list(problem.goal().predicates())),
    )
    return pddl


class PddlDomainFile:

    def __init__(self, domain, round_costs=0):
        self.pddl = pddl_domain(domain, round_costs)
        self.prefix = '{}__'.format(domain['name'])
        self.filename = None

    def __enter__(self):
        with NamedTemporaryFile(prefix=self.prefix, suffix='.pddl', delete=False) as f:
            f.write(bytes(self.pddl, 'ascii'))
            self.filename = f.name
        return self

    def __exit__(self, *args):
        os.remove(self.filename)
        self.filename = None


class PddlProblemFile:

    def __init__(self, problem):
        self.pddl = pddl_problem(problem)
        self.prefix = '{}__{}__'.format(problem['domain'], problem['name'])
        self.filename = None

    def __enter__(self):
        with NamedTemporaryFile(prefix=self.prefix, suffix='.pddl', delete=False) as f:
            f.write(bytes(self.pddl, 'ascii'))
            self.filename = f.name
        return self

    def __exit__(self, *args):
        os.remove(self.filename)
        self.filename = None


