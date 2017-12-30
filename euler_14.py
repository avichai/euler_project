# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.|

# Avichai Ben David

import sys
import eulerlib

MAX_VALUE = 1000000


def compute_chain_len(dic, i, max_chain, number_of_max_chain):
    tmp = i
    chain_len = 0

    chain_len = get_chain_len(chain_len, dic, tmp)
    dic[i] = chain_len

    if chain_len > max_chain:
        print("chain_len: {} and number: {}".format(chain_len, i))
        max_chain, number_of_max_chain = chain_len, i
    return max_chain, number_of_max_chain


def get_chain_len(chain_len, cache, tmp):
    while tmp != 1:
        if tmp in cache:
            chain_len += cache[tmp]
            break
        else:
            chain_len += 1
            if tmp % 2 == 0:  # tmp is even
                tmp /= 2
            else:
                tmp = 3 * tmp + 1
    if tmp == 1:
        chain_len += 1
    return chain_len


def compute():
    cache = {1: 1}
    max_chain = 1
    number_of_max_chain = 1
    for i in range(2, MAX_VALUE + 1):
        max_chain, number_of_max_chain = compute_chain_len(cache, i, max_chain, number_of_max_chain)

    return number_of_max_chain


@eulerlib.Memoize
def collatz_chain_length(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x / 2
    else:
        y = 3 * x + 1

    return collatz_chain_length(y) + 1


def compute2():
    sys.setrecursionlimit(3000)
    return max(range(1, MAX_VALUE), key=collatz_chain_length)


if __name__ == "__main__":
    # print("Number with max chain: {}".format(compute()))
    print("Number with max chain: {}".format(compute2()))
