# 1000-digit Fibonacci number

# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from itertools import count

NUM_DIG = 1000


def compute():
    f_n = 1
    f_n_plus_one = 1
    index = 2

    while f_n_plus_one // (10 ** (NUM_DIG - 1)) == 0:
        f_n, f_n_plus_one = f_n_plus_one, f_n + f_n_plus_one
        index += 1
    return index


def compute2():
    f_n = 1
    f_n_plus_one = 1

    for i in count(start=2):
        num_digs = len(str(f_n_plus_one))
        if num_digs > NUM_DIG:
            raise RuntimeError("Not found")
        elif num_digs == NUM_DIG:
            return i
        f_n, f_n_plus_one = f_n_plus_one, f_n + f_n_plus_one


if __name__ == "__main__":
    print("The index of the first term in the Fibonacci sequence to contain 1000 digits is: {}".format(compute()))
    print("The index of the first term in the Fibonacci sequence to contain 1000 digits is: {}".format(compute2()))
