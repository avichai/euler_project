# Sum square difference

# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of
# the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Avichai Ben David


def square_of_sum(n):
    ret = sum(i for i in range(1, n + 1))
    return ret ** 2


def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))


def square_of_sum1(n):
    return (n * (n + 1) / 2) ** 2


def sum_of_squares1(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


if __name__ == "__main__":
    N = 100
    print(square_of_sum1(N) - sum_of_squares1(N))
    print(square_of_sum(N) - sum_of_squares(N))
