from random import *


class Iterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is not None:
            val = self.current.data
            self.current = self.current.next
            return val
        raise StopIteration


def generator(size, a, b):
    for i in range(size):
        yield randint(a, b)
