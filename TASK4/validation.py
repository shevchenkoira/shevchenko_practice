from linked_list import *
from iterator import *


def validate_number(text: str, msg):
    while True:
        try:
            num_inp = int(input(text))
            return num_inp
        except ValueError:
            print(msg["bad_num"])


def validate_index(ll, msg):
    while True:
        try:
            index = validate_number(msg["index"], msg)
            if index < 0 or index > ll.get_length():
                raise ValueError
            break
        except ValueError:
            print(msg["bad_index"])
    return index


def validate_size(msg):
    while True:
        try:
            size = validate_number(msg["size"], msg)
            if size <= 0:
                raise ValueError
            break
        except ValueError:
            print(msg["bad_size"])
    return size


def fill_from_keyboard(size, msg):
    ll = LinkedList()
    for i in range(0, size):
        ll.insert_at_end(validate_number(msg["value"], msg))
    return ll


def random_fill(size, start, end):
    ll = LinkedList()
    for i in range(0, size):
        ll.insert_at_end(randint(start, end))
    return ll


def random_generate(size, start, end):
    ll = LinkedList()
    ll.insert_at_end(generator(size, start, end))
    return ll

