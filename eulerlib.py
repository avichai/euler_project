import math


# Returns a list of True and False indicating whether each number is prime.
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.
def list_primality(n):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


# Returns all the prime numbers less than or equal to n, in ascending order.
# For example: listPrimes(97) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 83, 89, 97].
def list_primes(n):
    return [i for (i, is_prime) in enumerate(list_primality(n)) if is_prime]


def get_list_primes(n_of_primes):
    n = 3
    lst = [2]
    while len(lst) < n_of_primes:
        if is_prime(n):
            lst.append(n)
        n += 2
    return lst


def is_prime(n):
    for t in range(2, int(math.sqrt(n) + 1)):
        if n % t == 0 and n != t:
            return False
    return True


def get_sum_divisors(LIM):
    # compute sum of proper divisor for each number
    sum_divisors = [0] * LIM
    for i in range(1, len(sum_divisors)):
        for j in range(i * 2, len(sum_divisors), i):
            sum_divisors[j] += i
    return sum_divisors


# cache
class Memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        if args in self.cache:
            return self.cache[args]
        else:
            val = self.func(*args)
            self.cache[args] = val
            return val
