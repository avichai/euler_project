# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# Avichai Ben David

import itertools
import time
import eulerlib


def compute_last_prime(n_of_primes):
    n = 3
    l = [2]
    while len(l) < n_of_primes:
        if eulerlib.is_prime(n):
            l.append(n)
        n += 2
    return l[len(l) - 1]


def compute(n):
    return next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), n, None))


if __name__ == "__main__":
    before = int(round(time.time() * 1000))
    print(compute_last_prime(10001))
    after = int(round(time.time() * 1000))
    print(after - before)
    # print(compute(10000))
