# Factorial digit sum

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# Avichai Ben David


from math import factorial


def compute():
    return sum(int(c) for c in str(factorial(100)))


if __name__ == "__main__":
    print(compute())
