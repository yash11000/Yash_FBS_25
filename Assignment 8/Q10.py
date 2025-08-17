# Write a program to check if entered year is a leap year or not.
from operator import truediv


def leap_year():
    if (year % 4==0 and year % 100!=0)or (year %400==0):
        return True
    else:
        return False
year = int(input("Enter the year here : "))

leap_year()

if leap_year():
    print(year,'This is a leap year')
else:
    print(year,'This is not a leap year')
