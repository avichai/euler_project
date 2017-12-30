# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# Avichai Ben David

import math

import eulerlib

NUMBER = 2000000


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and n != i:
            return False

    return True


def compute(n):
    res = 2
    for i in range(3, n, 2):
        if is_prime(i):
            res += i
    return res


def compute1(n):
    return sum(eulerlib.list_primes(n))


if __name__ == "__main__":
    print(compute1(NUMBER))
    # print(compute(NUMBER))
