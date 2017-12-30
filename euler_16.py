# Power digit sum

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

# Avichai Ben David

EXPONENT = 1000
BASE = 2


def compute():
    str_num = str(BASE ** EXPONENT)
    res = sum(int(c) for c in str_num)
    return res


if __name__ == "__main__":
    print(compute())
