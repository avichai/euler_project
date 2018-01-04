# Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are 
# called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

# Avichai Ben David
import math

from eulerlib import get_sum_divisors

LIM = 10000


def sum_div_of_num(num):
    return sum(j for j in range(1, num // 2 + 1) if num % j == 0)


def sum_div_of_num_efficient(num):
    if num == 1:
        return 0
    else:
        r = math.floor(math.sqrt(num))
        res = 1 + r if r * r == num else 1
        if num % 2 != 0:
            f = 3
            step = 2
        else:
            f = 2
            step = 1
        while f < r:
            res += (f + num // f) if num % f == 0 else 0
            f += step
        return res


def compute():
    amicable_set = set()
    sum_divisors = {}
    for num in range(2, LIM):
        sum_divisors[num] = sum_div_of_num_efficient(num)
    for key_1 in sum_divisors.keys():
        for key_2 in sum_divisors.keys():
            if sum_divisors[key_1] == key_2 and sum_divisors[key_2] == key_1 and key_1 != key_2:
                amicable_set.add(key_1)
    return sum(amicable for amicable in amicable_set)


def compute2():
    sum_divisors = get_sum_divisors(LIM)

    # find all amicable pairs within range
    res = 0
    for i in range(1, len(sum_divisors)):
        j = sum_divisors[i]
        res += i if j != i and j < len(sum_divisors) and sum_divisors[j] == i else 0
    return res


def compute3():
    res = 0
    for num_1 in range(2, LIM):
        num_2 = sum_div_of_num_efficient(num_1)
        if num_2 > num_1 and sum_div_of_num_efficient(num_2) == num_1:
            res += num_1 + num_2
    return res


if __name__ == "__main__":
    print(compute2())  # much more efficient
    print(compute3())
    print(compute())
