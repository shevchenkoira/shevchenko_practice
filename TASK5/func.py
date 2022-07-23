from validation import *
from strategy import *


def command1(msg):
    size = validate_size(msg)
    start = validate_number(msg["start_num"], msg)
    end = validate_number(msg["end_num"], msg)
    if start > end:
        start, end = end, start
    return size, start, end


def command4(ll, msg):
    if not (ll.is_empty()):
        index = validate_index(ll, msg)
        ll.remove_at(index)
        ll.print()
    else:
        print(msg["empty"])


def command5(ll, msg):
    if not (ll.is_empty()):
        start = validate_index(ll, msg)
        end = validate_index(ll, msg)
        if start > end:
            start, end = end, start
        ll.remove_range_of_nodes(start, end)
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


def command7(msg, command, ll):
    while True:
        index = validate_index(ll, msg)
        if command == "1":
            temp = command1(msg)
            ll = Context(Strategy1()).execute_strategy(temp[0], temp[1], temp[2], ll, index)
            return ll
        elif command == "2":
            file_name = validate_file_input(msg)
            ll = Context(Strategy2()).execute_strategy(file_name, ll, index)
            return ll
        else:
             print(msg["bad_choice"])


def menu():
    messages = {
        "choices": "Available commands: \n 0 - finish work \n 1 - strategy 1 \n 2 - strategy 2 \n 3 - generate list \n"
                   " 4 - remove element at k-position \n 5 - remove element in some range \n 6 - do task \n 7 - print",
        "not_available": "This command is not available now, please, firstly, choose strategy",
        "bad_choice": "There is no such command, please, try again",
        "element": "Enter element ",
        "start_num": "Enter start num ",
        "end_num": "Enter end num ",
        "bad_num": "You didn't enter a number, try again",
        "index": "Enter k-position ",
        "bad_index": "Try again, your index is lower than 0 or bigger than your list`s size",
        "size": "Enter size of your Linked List ",
        "bad_size": "Try again, your size is lower than 0",
        "value": "Enter value you want to insert ",
        "nothing": "Nothing changed:",
        "empty": "List is empty",
        "name_file": "Input name of your file: ",
        "file_not_exist": "File not exists, try again",
        "bad_file": "Your file contains letter, try another one"

    }
    ll = LinkedList()
    flag = False
    while True:
        print(messages["choices"])
        command_input = input()
        if command_input == "0":
            break
        elif command_input == "1" or command_input == "2":
            strateg = command_input
            flag = True
            continue
        if flag:
            if command_input == "3":
                command7(messages, strateg, ll)
            elif command_input == "4":
                command4(ll, messages)
            elif command_input == "5":
                command5(ll, messages)
            elif command_input == "6":
                command6(ll, messages)
            elif command_input == "7":
                ll.print()
            else:
                print(messages["bad_choice"])
        else:
            print(messages["not_available"])
