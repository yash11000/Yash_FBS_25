# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def exponential():
    sum = 0
    expo = 1
    for i in range(1,n+1):
        expo = i**i
        sum = expo+sum
    return sum
n = int(input("Enter the last number here : "))
res = exponential()
print(res)