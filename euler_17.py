# Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
# out numbers is in compliance with British usage.

# Avichai Ben Daivd

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

DIC = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety", 1000: "onethousand"
}

HUNDRED = "hundred"
THOUSAND = "thousand"
AND = "and"

LIM = 1000


def count_letters_of_num(n):
    if n in DIC:
        return DIC[n]
    ones = n % 10
    if len(str(n)) == 2:
        tens = n // 10 * 10
        return DIC[tens] + DIC[ones]
    elif len(str(n)) == 3:
        hundreds = n // 100
        tens_ones = n % 100
        if tens_ones in DIC:
            tens = tens_ones
            return DIC[hundreds] + HUNDRED + ((AND + DIC[tens]) if tens != 0 else "")
        else:
            tens = tens_ones // 10 * 10
            return DIC[hundreds] + HUNDRED + AND + DIC[tens] + DIC[ones]


def count_letters_of_num1(n):
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ONES[n // 100] + HUNDRED + ((AND + count_letters_of_num1(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 10000:
        return count_letters_of_num1(n // 1000) + THOUSAND + (
            count_letters_of_num1(n % 1000) if (n % 1000 != 0) else "")


def compute():
    return sum(len(count_letters_of_num(i)) for i in range(1, LIM + 1))
    # return sum(len(count_letters_of_num1(i)) for i in range(1, LIM + 1))


if __name__ == "__main__":
    print("If all the numbers from 1 to {} inclusive were written out in words, "
          "we will use {} letters".format(LIM, compute()))
