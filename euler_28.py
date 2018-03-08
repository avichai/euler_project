# Number spiral diagonals

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Avichai Ben David

SIZE = 1001


# From the diagram, let's observe the four corners of an n * n square (where n is odd).
# It's not hard to convince yourself that the top right corner always has the value n^2.
# Working counterclockwise (backwards), the top left corner has the value n^2 - (n - 1),
# the bottom left corner has the value n^2 - 2(n - 1), and the bottom right is n^2 - 3(n - 1).
# Putting it all together, this outermost ring contributes 4n^2 - 6(n - 1) to the final sum.
#
# Incidentally, the closed form of this sum is (4m^3 + 3m^2 + 8m - 9) / 6, where m = size.
def compute():
    ans = 1
    ans += sum((4 * i * i - 6 * (i - 1) for i in range(3, SIZE + 1, 2)))
    return ans


if __name__ == "__main__":
    print(compute())
