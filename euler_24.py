# Lexicographic permutations

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Avichai Ben David

from itertools import islice
from itertools import permutations

DIGITS_STR = '0123456789'
PERM_NUM = 1000000
NUM_DIG = 10


def compute():
    p = islice(permutations(DIGITS_STR, len(DIGITS_STR)), PERM_NUM - 1, None)
    return "".join(x for x in next(p))


def compute1():
    arr = list(range(NUM_DIG))
    perm = islice(permutations(arr), PERM_NUM - 1, None)
    return "".join(str(x) for x in next(perm))


if __name__ == "__main__":
    print(compute())
    print(compute1())
