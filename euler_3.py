# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Avichai Ben David

import math

NUMBER_TO_TEST = 600851475143


def smallest_prime_factor(n):
    assert n >= 2

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i

    return n


def compute(n):
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n /= p
        else:
            return n


if __name__ == "__main__":
    print(compute(NUMBER_TO_TEST))
