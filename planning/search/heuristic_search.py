from copy import deepcopy

from .search import FOUND, NOT_FOUND, UNSOLVABLE
from .search import Search
from .search import SearchNode
from .search import reconstruct_path
from .heuristics import NullHeuristic
from .priority_queue import PriorityQueue


class BestFirstSearch(Search):

    def _run_search(self):
        node_bound = self._parameters.get("node_bound", None)
        close_forever = self._parameters.get("close_forever", True)
        heuristic = self._parameters.get("heuristic", NullHeuristic())
        heuristic.reset()
        init = self._problem.init()
        goal = self._problem.goal()
        wrapped_init = SearchNode(init)
        wrapped_init.update_priority(heuristic)
        q = PriorityQueue(wrapped_init)
        closed = set()
        tree = {init: (None, None)}
        cost_so_far = {init: wrapped_init.priority}
        operators = self._problem.operators()
        while q:
            node = q.pop()
            acc_cost = node.accumulated_cost
            state = node.state
            # next, we discard outdated items of the queue
            if close_forever:
                if state in closed:
                    continue
                closed.add(state)
            if state.entails(goal):
                self._plan = reconstruct_path(tree, state)
                self._info["generated"] = len(tree) - 1
                return FOUND
            for op, wrapped_succ in node:
                succ = wrapped_succ.state
                if close_forever and succ in closed:
                    continue
                wrapped_succ.update_priority(heuristic)
                cost_to_succ = cost_so_far.get(succ, None)
                if cost_to_succ is None or wrapped_succ.priority < cost_to_succ:
                    cost_so_far[succ] = wrapped_succ.priority
                    tree[succ] = (state, op)
                    q.push(wrapped_succ)
            if node_bound and len(tree) > node_bound:
                self.log("Node bound exceeded ({}>{})".format(len(tree), node_bound))
                return NOT_FOUND
            if self._stop_timeout:
                self.log("Timeout")
                return NOT_FOUND
        return UNSOLVABLE


# class AStarSearch(Search):

    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # epsilon = 

