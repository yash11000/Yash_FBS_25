# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n


def addition ():
    sum = 0
    for i in range(0,n+1):
        sum = sum + i

    return sum

n = int(input("Enter the last number here : "))

res = addition()
print("The sum is", res)