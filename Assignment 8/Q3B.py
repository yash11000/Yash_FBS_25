# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n


def factorial():
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        sum = sum + fact
    return sum

n = int(input("Enter the last number here : "))

res = factorial()

print(res)