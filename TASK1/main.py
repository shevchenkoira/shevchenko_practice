def input_num():
    while True:
        try:
            new_num = int(input("Enter number needed: "))
            if new_num < 0:
                raise ValueError
            return new_num
        except ValueError:
            print("Try again")


def print_out_quantity_of_happy_numbers(a: int):
    k = 0
    a = str(a)
    n = len(a)
    sum = 0
    for i in range(n):
        val = int(a[i])
        if val < 4:
            break
        if val > 7:
            k = 1 if k == 0 else k
            k *= 2**(n - i)
            break
        if 4 < val < 7:
            k = 1 if k == 0 else k
            k *= 2**(n - i - 1)
            break
        if val == 7:
            sum += 2 ** (n - i - 1)
        if val == 4:
            continue
    else:
        k = 1 if k == 0 else k

    return k + sum


def remove_if():
    end_num = input_num()
    nums_quantity = 0
    for i in range(1, len(str(end_num))):
        nums_quantity += 2**i
    return nums_quantity + print_out_quantity_of_happy_numbers(end_num)


print(remove_if())
