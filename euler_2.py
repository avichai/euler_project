# Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Avichai Ben David

MAX_VALUE = 4000000


def compute():
    res = 0

    i = 0
    j = 1

    while j <= MAX_VALUE:
        if j % 2 == 0:
            res += j

        tmp = j
        j += i
        i = tmp
    return res


if __name__ == "__main__":
    print(compute())
