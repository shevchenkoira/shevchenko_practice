def input_num():
    while True:
        try:
            new_num = int(input("Enter number needed: "))
            if new_num < 0:
                raise ValueError
            return new_num
        except ValueError:
            print("Try again")


def fill_arr_to_check():
    while True:
        try:
            size_arr = int(input("Enter size of your array: "))
            if size_arr <= 0:
                raise ValueError
            my_arr = [int(input("Enter" + " " + str(i) + " " + "number: ")) for i in range(size_arr)]
            return my_arr
        except ValueError:
            print("You didn't enter a number, try again from the beginning")


def bigger_than(arr_to_check: [], num: int):
    count = 0
    for i in arr_to_check:
        if num > i:
            count += 1
    return count


def cout_after_nnumber(our_values: [], a: int):
    count_after = 0
    for i in range(len(str(a))):
        count_after += bigger_than(our_values, int(str(a)[i]))*(len(our_values)**(len(str(a))-i-1))
        if not(int(str(a)[i]) in our_values):
            break
        if i == len(str(a)) - 1:
            count_after = 1 if count_after == 0 else count_after

    return count_after


def happy_numbers(our_values: []):
    end_value = input_num()
    nums_quantity = 0
    for i in range(1, len(str(end_value))):
        nums_quantity += len(our_values)**i
    return nums_quantity + cout_after_nnumber(our_values, end_value)


our_values = fill_arr_to_check()
print(happy_numbers(our_values))
