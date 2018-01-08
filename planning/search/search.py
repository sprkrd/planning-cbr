from time import clock
from threading import Timer
from threading import Lock

from copy import copy

FOUND = 1
NOT_FOUND = 0
UNSOLVABLE = -1


class Search:

    def __init__(self, problem, timeout=None, verbose=0, **parameters):
        self._problem = problem
        self._timeout = timeout
        self._verbose = verbose
        self._parameters = parameters
        self._start = None
        self._elapsed = 0.0
        self._stop_timeout = False
        self._plan = None
        self._info = {}

    def _trigger_timeout(self):
        self._stop_timeout = True

    def __call__(self):
        self._start = clock()
        if self._timeout:
            timer = Timer(self._timeout, self._trigger_timeout)
            timer.start()
        if self._problem.trivial():
            status = FOUND
            self._plan = [(self._problem.goal(), None)]
        else:
            status = NOT_FOUND
        status = self._run_search()
        if self._timeout and not self._stop_timeout:
            # cancel timeout
            timer.cancel()
        if status == FOUND:
            plan_len = len(self._plan) - 1
            self.log("Plan found with {} action(s)".format(plan_len))
        elif status == UNSOLVABLE:
            self.log("Unsolvable")
        elif status == NOT_FOUND:
            self.log("Could not find solution")
        self._elapsed = clock() - self._start
        return status

    def log(self, msg, level=1):
        if level <= self._verbose:
            elapsed = clock() - self._start
            print("[{:.03f}s] ".format(elapsed) + str(msg))

    def plan(self):
        return list(map(lambda t: t[1], self._plan[:-1]))

    def state_sequence(self):
        return list(map(lambda t: t[0], self._plan))

    def info(self):
        return self._info

    def elapsed(self):
        return self._elapsed

    def _run_search(self):
        raise NotImplementedError()


class SearchNode:

    def __init__(self, state, priority=None, accumulated_cost=0, relaxed_goal=None):
        self.priority = priority
        self.state = state
        self.accumulated_cost = accumulated_cost
        self.relaxed_goal = None

    def update_priority(self, heuristic):
        self.priority = heuristic(self)

    def __lt__(self, other):
        return self.priority < other.priority

    def __iter__(self):
        state = self.state
        operators = state.problem().operators()
        for op in operators:
            successor = state.apply(op)
            if successor:
                acc_cost = self.accumulated_cost + op.cost()
                wrapped_succ = SearchNode(successor, accumulated_cost=acc_cost)
                wrapped_succ.relaxed_goal = copy(self.relaxed_goal)
                yield op, wrapped_succ

    def __str__(self):
        return "[{}] {}".format(self.priority, self.state)


def reconstruct_path(tree, goal):
    parent, op = goal, None
    plan = []
    while parent is not None:
        plan.append((parent, op))
        parent, op = tree[parent]
    plan.reverse()
    return plan

