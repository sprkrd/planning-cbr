from .fifo_queue import Queue
from .search import FOUND, NOT_FOUND, UNSOLVABLE
from .search import Search
from .search import reconstruct_path


class BreadthFirstSearch(Search):

    def _run_search(self):
        node_bound = self._parameters.get("node_bound", None)
        init = self._problem.init()
        goal = self._problem.goal()
        q = Queue(init)
        tree = {init: (None, None)}
        operators = self._problem.operators()
        while q:
            state = q.pop()
            for op in operators:
                successor = state.apply(op)
                if successor and successor not in tree:
                    tree[successor] = (state, op)
                    if successor.entails(goal):
                        self._plan = reconstruct_path(tree, successor)
                        self._info["generated"] = len(tree) - 1
                        return FOUND
                    q.push(successor)
            if node_bound and len(tree) > node_bound:
                self.log("Node bound exceeded ({}>{})".format(len(tree), node_bound))
                return NOT_FOUND
            if self._stop_timeout:
                self.log("Timeout")
                return NOT_FOUND
        return UNSOLVABLE


class IterativeDeepeningSearch(Search):

    def ids(self, depth, plan=None, visited=None, history=None):
        plan = plan or []
        history = history or [self._problem.init()]
        visited = visited or set(history)
        goal = self._problem.goal()
        operators = self._problem.operators()
        state = history[-1]
        if state.entails(goal):
            return list(zip(history, plan+[None]))
        if depth <= 0 or self._stop_timeout:
            return None
        for op in operators:
            successor = state.apply(op)
            if successor and successor not in visited:
                plan.append(op)
                history.append(successor)
                visited.add(successor)
                p = self.ids(depth-1, plan, visited, history)
                if p is not None:
                    return p
                plan.pop()
                history.pop()
                visited.remove(successor)
        return None

    def _run_search(self):
        initial_depth = self._parameters.get("initial_depth", 1)
        max_depth = self._parameters.get("max_depth", 10000)
        n_visited = 0
        for depth in range(initial_depth, max_depth+1):
            self.log("Trying depth {}...".format(depth))
            plan = self.ids(depth)
            if plan:
                self._plan = plan
                return FOUND
            elif self._stop_timeout:
                self.log("Timeout")
                break
        return NOT_FOUND

