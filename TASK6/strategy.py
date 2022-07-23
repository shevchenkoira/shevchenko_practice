from abc import *
from validation import *
from linked_list import *


class Strategy(metaclass=ABCMeta):
    def do_operation(self, *args):
        pass


class Strategy1(Strategy):
    def do_operation(self, size, start, end, ll, index):
        ls = random_generate(size, start, end)
        ll.insert_list(index, ls)
        return ll


class Strategy2(Strategy):
    def do_operation(self, file_name, ll, index):
        f = open(file_name, 'r')
        ls = LinkedList()
        for i in ''.join(f.readlines()).split():
            ls.insert_at_end(int(i))
        ll.insert_list(index, ls)
        return ll


class Context:
    def __init__(self, strategy):
        self.__strategy = strategy

    def execute_strategy(self, *args):
        return self.__strategy.do_operation(*args)

