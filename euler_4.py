# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Avichai Ben David


def is_palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def compute():
    largest_pali = 1

    for i in range(1, 1000):
        for j in range(1, 1000):
            if is_palindrom(i * j) and i * j > largest_pali:
                largest_pali = i * j
    return largest_pali


if __name__ == "__main__":
    print(compute())
