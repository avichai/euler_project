# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Avichai Ben David

import datetime

DAYS_FAB_REG = 28
DAYS_FAB_LEAP = 29

LAST_YEAR = 2000
START_YEAR = 1900
NUM_MONTH = 12
LEAP = 0

SUNDAY_INDEX = 6

months_reg = {0: 31, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}

first_sunday = "7 of january 1900"


def compute():
    count_sundays = 0
    count_days = 6
    month = 0
    year = START_YEAR
    leap = 0

    while year != LAST_YEAR + 1:
        if year != START_YEAR and count_days == 0:
            count_sundays += 1

        count_days += 7

        if month in months_reg:
            count_days, leap, month, year = update_reg_month(count_days, leap, month, year)

        else:
            count_days, month = update_february(count_days, leap, month, year)
    return count_sundays


def update_february(count_days, leap, month, year):
    if leap == LEAP and year != START_YEAR:
        if DAYS_FAB_LEAP <= count_days:
            month += 1
            count_days %= DAYS_FAB_LEAP
    elif DAYS_FAB_REG <= count_days:
        month += 1
        count_days %= DAYS_FAB_REG
    return count_days, month


def update_reg_month(count_days, leap, month, year):
    if months_reg[month] <= count_days:
        if month == NUM_MONTH - 1:
            year += 1
            leap += 1
            leap %= 4
        count_days %= months_reg[month]
        month += 1
        month %= NUM_MONTH
    return count_days, leap, month, year


def compute2():
    return sum(1
               for y in range(START_YEAR + 1, LAST_YEAR + 1)
               for m in range(1, NUM_MONTH + 1)
               if datetime.date(y, m, 1).weekday() == SUNDAY_INDEX)


if __name__ == "__main__":
    print(compute())
    print(compute2())