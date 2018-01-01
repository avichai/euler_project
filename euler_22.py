# Names scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#  begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
#  value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
#  the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

# Avichai Ben David

LETTER_TO_NUM = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                 'X': 24, 'Y': 25, 'Z': 26}

FILE_LOCATION = "./Resources/euler_22_names.txt"  # path to file
DELIMITER = ','


def initialize_input():
    names_file = open(FILE_LOCATION)
    return sorted(names_file.read().replace("\"", "").split(DELIMITER))


def compute2():
    return sum((ord(c) - ord('A') + 1) * (i + 1)
               for (i, name) in enumerate(sorted(names))
               for c in name)


def compute():
    return sum(sum(LETTER_TO_NUM[c] for c in names[i]) * (i + 1) for i in range(len(names)))


if __name__ == "__main__":
    names = initialize_input()
    print(compute())
    print(compute2())
