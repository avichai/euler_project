# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Avichai Ben David


PERIMETER = 1000


def compute(n):
    for i in range(1, (n - 3) // 3 + 1):
        for j in range(i + 1, (n - 1 - i) // 2 + 1):
            l = 1000 - j - i
            if i ** 2 + j ** 2 == l ** 2:
                print('i: {}, j: {}, l: {}'.format(i, j, l))
                return i * j * l
    return -1


if __name__ == "__main__":
    print(compute(PERIMETER))
