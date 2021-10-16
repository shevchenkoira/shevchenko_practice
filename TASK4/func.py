from validation import *


def command1(msg):
    size = validate_size(msg)
    ll = fill_from_keyboard(size, msg)
    ll.print()
    return ll


def command2(msg):
    size = validate_size(msg)
    start = validate_number(msg["start_num"], msg)
    end = validate_number(msg["end_num"], msg)
    ll = random_fill(size, start, end)
    ll.print()
    return ll


def command3(msg):
    size = validate_size(msg)
    start = validate_number(msg["start_num"], msg)
    end = validate_number(msg["end_num"], msg)
    ll = LinkedList()
    my_gen = generator(size, start, end)
    for i in my_gen:
        ll.insert_at_end(i)
    ll.print()
    return ll


def command4(ll, msg):
    if not(ll.is_empty()):
        index = validate_index(ll, msg)
        data = validate_number(msg["element"], msg)
        ll.insert_at(index, data)
        ll.print()
    else:
        print(msg["empty"])


def command5(ll, msg):
    if not (ll.is_empty()):
        index = validate_index(ll, msg)
        ll.remove_at(index)
        ll.print()
    else:
        print(msg["empty"])


def command6(ll, msg):
    if not (ll.is_empty()):
        if not(ll.is_falling() or ll.is_raising()):
            ll.remove_if_multiple(4)
            ll.print()
        else:
            print(msg["nothing"])
            ll.print()
    else:
        print(msg["empty"])


def command7(msg):
    while True:
        print(msg["create_list"])
        create_command = input()
        if create_command == "a":
            ll = command2(msg)
            return ll
        elif create_command == "b":
            ll = command3(msg)
            return ll
        elif create_command == "c":
            ll = command1(msg)
            return ll
        else:
             print(msg["bad_choice"])


def menu():
    messages = {
        "choices": "Available commands: \n 0 - finish work \n 1 - create list \n 2 - insert element at k-position "
                   "\n 3 - remove element at k-position \n 4 - do task",
        "create_list": "a - create using random \n b - create using iterator \n c - create using keyboard \n",
        "not_available": "This command is not available now, please, firstly, create list",
        "bad_choice": "There is no such command, please, try again",
        "element": "Enter element ",
        "start_num": "Enter start num for random ",
        "end_num": "Enter end num for random ",
        "bad_num": "You didn't enter a number, try again",
        "index": "Enter k-position ",
        "bad_index": "Try again, your index is lower than 0 or bigger than your list`s size",
        "size": "Enter size of your Linked List ",
        "bad_size": "Try again, your size is lower than 0",
        "value": "Enter value you want to insert ",
        "nothing": "Nothing changed:",
        "empty": "List is empty"
    }
    ll = LinkedList()
    flag = False
    while True:
        print(messages["choices"])
        command_input = input()
        if command_input == "0":
            break
        elif command_input == "1":
            ll = command7(messages)
            flag = True
            continue
        if flag:
            if command_input == "2":
                command4(ll, messages)
            elif command_input == "3":
                command5(ll, messages)
            elif command_input == "4":
                command6(ll, messages)
            else:
                print(messages["bad_choice"])
        else:
            print(messages["not_available"])
