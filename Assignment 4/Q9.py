# Q9 WAP to print all numbers in a range divisible by a given number.

n = int(input("Enter the range here : "))
num = int(input("Enter the divisior number here : "))

for i in range(1,n+1):
    if i%num==0:
        print(i)