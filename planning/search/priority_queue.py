from heapq import heappush, heappop, heapify


class PriorityQueue:

    def __init__(self, *items):
        self._heap = list(items)
        heapify(self._heap)

    def pop(self):
        return heappop(self._heap)

    def push(self, item):
        heappush(self._heap, item)

    def __len__(self):
        return len(self._heap)

    def __bool__(self):
        return bool(self._heap)

    def __str__(self):
        return "Heap: {}".format(",".join(map(str, self._heap)))


if __name__ == "__main__":
    q = PriorityQueue(5, 0, 6, -1)
    q.push(-2)
    q.push(2)
    while q:
        print(q.pop())

