#!/usr/bin/env python3
year = int(input("Enter a year: "))
def is_leap(year):
    leap = False
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
if is_leap(year) == False:
    print("The year " + str(year) + " --> NOT a leap year")
else:
    print("The year " + str(year) + " --> a leap year")