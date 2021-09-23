import random

def inp_number(text: str, reverse_flag: bool):
    while True:
        try:
            num_inp = int(input(text))
            if reverse_flag:
                if num_inp <= 0:
                    raise ValueError
            return num_inp
        except ValueError:
            print("You didn't enter a number, try again from the beginning")


def fill_matrix(matrix_size: int):
    matrix_main = [[] for i in range(matrix_size)]
    for i in range(len(matrix_main)):
        for j in range(matrix_size):
            while True:
                try:
                    matrix_main[i].insert(j, int(input("a[" + str(i + 1) + "][" + str(j + 1) + "] = ")))
                    break
                except ValueError:
                    print("Try again")
    return matrix_main


def random_matrix(matrix_size: int):
    while True:
        try:
            start_rand = inp_number("Enter a first number for random:", False)
            last_rand = inp_number("Enter a last number for random:", False)
            if start_rand >= last_rand:
                raise ValueError
            break
        except ValueError:
            print("Start > last, try again")
    matrix_main = [[] for i in range(matrix_size)]
    for i in range(len(matrix_main)):
        for j in range(matrix_size):
            matrix_main[i].insert(j, random.randint(start_rand, last_rand))
    return matrix_main


def bubble_sort(count_action, matrix_main):
    for i in range(len(matrix_main) - 1):
        for j in range(0, len(matrix_main) - i - 1):
            if matrix_main[j] > matrix_main[j + 1]:
                matrix_main[j], matrix_main[j + 1] = matrix_main[j + 1], matrix_main[j]
                count_action += 1
    return count_action


def sort(matrix_main):
    count_action = 0
    temp = [0] * (len(matrix_main) * len(matrix_main))
    k = 0
    for i in range(0, len(matrix_main)):
        for j in range(0, len(matrix_main)):
            temp[k] = matrix_main[i][j]
            k += 1
            count_action += 1
    count_action = bubble_sort(count_action, temp)
    k = 0
    for i in range(0, len(matrix_main)):
        for j in range(0, len(matrix_main)):
            matrix_main[i][j] = temp[k]
            k += 1
            count_action += 1
    print("Sort takes " + str(count_action) + " action")
    print(matrix_main)
    return matrix_main


def binary_search(matrix_size: int, element: int, array: []):
    left = 0
    matrix_size -= 1
    right = matrix_size
    while right - left > 1:
        mid = (right + left) // 2
        if array[mid] >= element:
            right = mid
        else:
            left = mid
    if array[left] == element:
        return left
    if array[right] == element:
        return right
    return None


def bin_find(matrix_size: int, target: int, matrix_main: []):
    iterator_y = 0
    matrix_main = sort(matrix_main)
    if not matrix_main or not matrix_main[0]:
        return False
    for row in matrix_main:
        i = binary_search(matrix_size, target, row)
        if i == None:
            iterator_y += 1
            continue
        if i < len(row) and row[i] == target:
            return f"Index of needed element is [{iterator_y + 1}][{i + 1}]"
    return "This element is not found"


while True:
    print("Available commands: \n exit - finish work \n fill matrix - fill matrix by keyboard \n random matrix - "
          " random matrix in a certain interval")
    command_input = input()
    if command_input == "exit":
        break
    elif command_input == "fill matrix" or command_input == "random matrix":
        size_matrix = inp_number("Enter your matrix size: ", True)
        if command_input == "fill matrix":
            matrix = fill_matrix(size_matrix)
        elif command_input == "random matrix":
            matrix = random_matrix(size_matrix)
        print(bin_find(size_matrix, inp_number("Enter a number you want to find: ", False), matrix))
        continue
    else:
        print("There is no such command, please, try again")


