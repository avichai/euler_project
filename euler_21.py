# Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are 
# called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

# Avichai Ben David

set
LIM = 10000


def sum_div_of_num(num):
    return sum(j for j in range(1, num // 2 + 1) if num % j == 0)


def compute():
    amicable_set = set()
    sum_divisors = {}
    for num in range(2, LIM):
        sum_divisors[num] = sum_div_of_num(num)
    for key_1 in sum_divisors.keys():
        for key_2 in sum_divisors.keys():
            if sum_divisors[key_1] == key_2 and sum_divisors[key_2] == key_1 and key_1 != key_2:
                amicable_set.add(key_1)
    return sum(amicable for amicable in amicable_set)


def compute2():
    sum_divisors = [0] * LIM
    # compute sum of proper divisor for each number
    for i in range(1, len(sum_divisors)):
        for j in range(i * 2, len(sum_divisors), i):
            sum_divisors[j] += i

    # find all amicable pairs within range
    res = 0
    for i in range(1, len(sum_divisors)):
        j = sum_divisors[i]
        res += i if j != i and j < len(sum_divisors) and sum_divisors[j] == i else 0
    return res


if __name__ == "__main__":
    print(compute2()) # much more efficient
    # print(compute())
