

class Node:
    def __init__(self, item, next_=None):
        self.item = item
        self.next_ = next_


class Queue:
    def __init__(self, *items):
        self.front_ = None
        self.last_ = None
        self.size_ = 0
        for item in items: self.push(item)
        
    def pop(self):
        assert self.front_ is not None
        if self.front_ is self.last_: self.last_ = None
        front = self.front_.item
        self.front_ = self.front_.next_
        self.size_ -= 1
        return front
    
    def push(self, item):
        last = Node(item)
        if self.last_: self.last_.next_ = last
        else: self.front_ = last
        self.last_ = last
        self.size_ += 1
        
    def front(self):
        assert self.front_ is not None
        return self.front_.item

    def __len__(self):
        return self.size_
    
    def __bool__(self):
        return self.front_ is not None
    
    def __str__(self):
        if self.front_ is None: return '(empty)'
        first = True
        current = self.front_
        ret = '['
        while current is not None:
            if not first: ret += ','
            ret += str(current.item)
            first = False
            current = current.next_
        ret += ']'
        return ret

