from iterator import *
from observer import *


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.root = None

    def insert_at_the_beginning(self, data):
        node = Node(data, self.root, None)
        self.root = node
        self.root.next.prev = node

    def insert_at_end(self, data):
        if self.root is None:
            self.root = Node(data, None, None)
            return
        else:
            itr = self.root
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None, itr)

    def get_length(self):
        count = 0
        itr = self.root
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_the_beginning(data)
        else:
            itr = self.root
            count = 0
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next, itr)
                    if node.next:
                        node.next.prev = node
                    itr.next = node
                    break
                else:
                    count += 1
                    itr = itr.next

    def insert_list(self, index, ll):
        itr = Iterator(ll.root)
        if self.get_length() != 0:
            counter = 0
            for elem in itr:
                self.insert_at(index + counter, elem)
                counter += 1
        else:
            for i in itr:
                self.insert_at_end(i)

    def remove_at(self, index):
        if index == 0:
            self.root = self.root.next
            self.root.prev = None
            return
        else:
            itr = self.root
            count = 0
            while itr:
                if count == index:
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev
                    break
                else:
                    count += 1
                    itr = itr.next

    def remove_range_of_nodes(self, start, end):
        if start > end:
            start, end = end, start
        deleted_list = []
        for node in range(start, end+1):
            deleted_list.append(self.find_at(node))
            self.remove_at(start)

    def find_at(self, index):
        itr = Iterator(self.root)
        counter = 0
        for i in itr:
            if counter == index:
                return i
            counter += 1

    def is_raising(self):
        itr = self.root
        while itr.next:
            if itr.data > itr.next.data:
                return False
            itr = itr.next
        else:
            return True

    def is_falling(self):
        itr = self.root
        while itr.next:
            if itr.data < itr.next.data:
                return False
            itr = itr.next
        else:
            return True

    def remove_if_multiple(self, multiple_num):
        count = self.get_length()
        for i in range(self.get_length()):
            if count % multiple_num == 0:
                self.remove_at(count)
            count -= 1

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def print(self):
        result_list = []
        if self.is_empty():
            return result_list
        else:
            node = self.root
            while node:
                result_list.append(node.data)
                node = node.next
        return result_list
