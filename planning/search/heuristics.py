

INF = float("inf") 


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


class AdditiveHeuristic(Heuristic):

    def __init__(self):
        self._cache = {}

    def hadd(self, state, goal):
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

    def __call__(self, node):
        state = node.state
        goal = state.problem().goal()
        cache = self._cache
        if state not in cache:
            cache[state] = self.hadd(state, goal)
        return cache[state]

    def reset(self):
        self._cache.clear()


class RelaxedPlanningGraphHeuristic(Heuristic):
    
    def __init__(self):
        self._cache = {}

    def rpg(self, state, goal):
        layer = set(state.predicates())
        target = goal.predicates()
        available_ops = state.problem().operators()
        # remaining_ops = []
        n_action_layers = 0
        fixpoint = False
        while not fixpoint and not target.issubset(layer):
            fixpoint = True
            next_layer = layer.copy()
            for op in available_ops:
                if layer.issuperset(op.pre_list()):
                    fixpoint = False
                    next_layer.update(op.add_list())
                # else:
                    # remaining_ops.append(op)
            # available_ops = remaining_ops
            # remaining_ops = []
            layer = next_layer
            n_action_layers += 1
        return INF if fixpoint else n_action_layers

    def __call__(self, node):
        state = node.state
        goal = state.problem().goal()
        cache = self._cache
        if state not in cache:
            cache[state] = self.rpg(state, goal)
        return cache[state]

    def reset(self):
        self._cache.clear()

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

