# Lattice path

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

# Avichai Ben David

from pprint import pprint

import math

ROWS = 20
COLS = 20
BEGIN_X = 0
BEGIN_Y = 0


def compute_num_paths(i, j):
    dic = {(i, j): 1}
    while i != ROWS or j != COLS:
        if i - 1 >= 0 and j - 1 >= 0:
            dic[(i, j)] = dic[(i - 1, j)] + dic[(i, j - 1)]
        elif i - 1 >= 0:
            dic[(i, j)] = dic[(i - 1, j)]
        elif j - 1 >= 0:
            dic[(i, j)] = dic[(i, j - 1)]
        if i < ROWS:
            i += 1
        else:
            i = 0
            j += 1
    dic[(ROWS, COLS)] = dic[(ROWS - 1, COLS)] + dic[(ROWS, COLS - 1)]
    pprint(dic)
    return dic[(ROWS, COLS)]


# This is a classic combinatorial problem. To get from the top left corner to the bottom right corner of an N*N grid,
# it involves making exactly N moves right and N moves down in some order. Because each individual down or right move
# is indistinguishable, there are exactly 2N choose N (binomial coefficient) ways of arranging these moves.
# Combination-based route-counting function, O(n) time and O(1) memory
def compute():
    return math.factorial(ROWS + COLS) / (math.factorial(ROWS) * math.factorial(COLS))


if __name__ == "__main__":
    print(compute_num_paths(BEGIN_X, BEGIN_Y))
    print(compute())
