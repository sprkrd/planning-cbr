import subprocess
import re
import os

from ..pddl_utility import PddlProblemFile, pddl_domain

from sklearn import neighbors

from .search import SearchNode

INF = float("inf") 

matcher = re.compile("Initial heuristic value for (\w+): (\d+)")

def call_fastdownward(domain_file, problem_file, *heuristics):
    heuristics = heuristics or ["add()"]
    cmd = ["fast-downward.py", domain_file, problem_file, "--search",
            "eager_greedy(["+",".join(heuristics)+"], bound=0)"]
    process = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = process.stdout.decode("ascii")
    heuristic_values = {}
    for m in matcher.finditer(out):
        name = m.group(1) + "()"
        value = m.group(2)
        heuristic_values[name] = float(value)
    return [heuristic_values[h] for h in heuristics]


class Heuristic:

    def __call__(self, node):
        raise NotImplementedError()

    def reset(self):
        pass


class NullHeuristic(Heuristic):

    def __call__(self, node):
        return 0


class GoalCountingHeuristic(Heuristic):

    def __call__(self, node):
        state = node.state
        goal = state.problem().goal()
        difference = goal.difference(state)
        return len(difference)


class RelaxedGoalCountingHeuristic(Heuristic):

    def __call__(self, node):
        state = node.state
        goal = state.problem().goal()
        if node.relaxed_goal is None:
            node.relaxed_goal = set(goal.predicates())
        relaxed_goal = node.relaxed_goal
        relaxed_goal.difference_update(state.predicates())
        return len(relaxed_goal)


class AccumulatedCost(Heuristic):

    def __call__(self, node):
        return node.accumulated_cost


class NoveltyHeuristic(Heuristic):

    def __init__(self):
        self._last_state = None
        self._cache = None

    def novelty(self, node):
        state = node.state
        last_state = self._last_state
        n = 0
        if not last_state:
            self._cache = set(node.state.predicates())
            self._last_state = state
            n = 1
        else:
            changes = state.predicates().symmetric_difference(last_state.predicates())
            if not changes.issubset(self._cache):
                n = 1
            self._cache.update(changes)
        self._last_state = state
        return n

    def reset(self):
        self._last_state = None
        self._cache = None

    def __call__(self, node):
        return 1 - self.novelty(node)


class IndexedNoveltyHeuristic(Heuristic):

    def __init__(self, heuristics):
        self._heuristics = heuristics
        self._novelty_dict = {}

    def novelty(self, node):
        h_value = tuple(h(node) for h in self._heuristics)
        if h_value not in self._novelty_dict:
            self._novelty_dict[h_value] = NoveltyHeuristic()
        n = self._novelty_dict[h_value](node)
        return n

    def __call__(self, node):
        return 1 - self.novelty(node)

    def reset(self):
        self._novelty_dict.clear()


class CachedHeuristic(Heuristic):
    
    def __init__(self):
        self._cache = {}

    def h(self, state, goal):
        raise NotImplementedError()

    def __call__(self, node):
        state = node.state
        goal = state.problem().goal()
        cache = self._cache
        if state not in cache:
            cache[state] = self.h(state, goal)
        return cache[state]

    def reset(self):
        self._cache.clear()


class AdditiveHeuristic(CachedHeuristic):

    def h(self, state, goal):
        hadd = {}
        for pred in state:
            hadd[pred] = 0
        fixpoint = False
        while not fixpoint:
            fixpoint = True
            for op in state.problem().operators():
                hadd_op = op.cost() + sum(hadd.get(pre,INF) for pre in op.pre_list())
                if hadd_op == INF:
                    continue
                for add in op.add_list():
                    if hadd_op < hadd.get(add,INF):
                        hadd[add] = hadd_op
                        fixpoint = False
        return sum(hadd.get(pred,INF) for pred in goal)


class RelaxedPlanningGraphHeuristic(CachedHeuristic):
    
    def h(self, state, goal):
        layer = set(state.predicates())
        target = goal.predicates()
        available_ops = state.problem().operators()
        remaining_ops = []
        n_action_layers = 0
        fixpoint = False
        while not fixpoint and not target.issubset(layer):
            fixpoint = True
            next_layer = layer.copy()
            for op in available_ops:
                if layer.issuperset(op.pre_list()):
                    fixpoint = False
                    next_layer.update(op.add_list())
                else:
                    remaining_ops.append(op)
            available_ops = remaining_ops
            remaining_ops = []
            layer = next_layer
            n_action_layers += 1
        return INF if fixpoint else n_action_layers


class FDHeuristic(CachedHeuristic):

    def __init__(self, domain, *heuristics):
        super().__init__()
        self._heuristics = list(heuristics)
        domains_folder = "domains_pddl"
        self._domain_file = os.path.join(domains_folder, domain.name()+".pddl")
        try:
            os.mkdir(domains_folder)
        except OSError:
            pass
        if not os.path.exists(self._domain_file):
            with open(self._domain_file, "w") as f:
                f.write(pddl_domain(domain))

    def h(self, state, goal):
        problem = state.problem()
        with PddlProblemFile(problem, state) as p:
            h = call_fastdownward(self._domain_file, p.filename, *self._heuristics)
        return h


class CBRHeuristic(Heuristic):
    
    def __init__(self, heuristic, X_0, y_0, **kwargs):
        self._heuristic = heuristic
        # prepare KNN regressor
        self._X = X_0
        self._y = y_0
        self._kwargs = kwargs
        k = kwargs.get("k", 3)
        weights = kwargs.get("weights", "distance")
        self._knn = neighbors.KNeighborsRegressor(k, weights)
        self._knn.fit(X_0, y_0)

    def __call__(self, node):
        h = self._heuristic(node)
        return self._knn.predict([h])[0]

    def reset(self):
        self._heuristic.reset()

    def update(self, search):
        new_X = []
        new_y = []
        plan_len = len(search.plan())
        for i, state in enumerate(search.state_sequence()):
            if i == plan_len:
                break
            h = self._heuristic(SearchNode(state))
            new_X.append(h)
            new_y.append(plan_len - i)
        self._X = np.r_[self._X, new_X]
        self._y = np.r_[self._y, new_y]
        self._knn.fit(self._X, self._y)


class LinearCombination(Heuristic):

    def __init__(self, heuristics, weights=None):
        weights = weights or (1,)*len(heuristics)
        self.heuristics = heuristics
        self.weights = weights

    def __call__(self, node):
        f = 0
        for h, w in zip(self.heuristics, self.weights):
            f += w*h(node)
        return f

    def reset(self):
        for h in self.heuristics:
            h.reset()


class ConcatenateHeuristic(Heuristic):

    def __init__(self, heuristics):
        self.heuristics = heuristics

    def __call__(self, node):
        return tuple(h(node) for h in self.heuristics)

    def reset(self):
        for h in self.heuristics:
            h.reset()


if __name__ == "__main__":
    # quick test
    import sys
    f1, f2 = sys.argv[1:3]
    heuristics = sys.argv[3:]
    print(call_fastdownward(f1, f2, *heuristics))

