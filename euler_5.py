# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Avichai Ben David

N = 20

import math


def evently_divisible(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i // math.gcd(ans, i)
    return ans


def evently_divisible_efficient(n, p):
    res = 1
    i = 0
    check = True
    limit = math.sqrt(n)
    a = p.copy()

    while i < len(p):
        a[i] = 1
        if check:
            if p[i] < limit:
                a[i] = math.floor(math.log(n) / math.log(p[i]))
            else:
                check = False
        res *= p[i] ** a[i]
        i += 1
    return res


def compute_primes_list(n):
    l = []
    for i in range(2, n + 1):
        to_add = True
        for t in range(2, int(math.sqrt(i) + 1)):
            if i % t == 0 and i != t:
                to_add = False
                break
        if to_add:
            l.append(i)
    return l


if __name__ == "__main__":
    p = compute_primes_list(N)
    print(evently_divisible(N))
    print(evently_divisible_efficient(N, p))
