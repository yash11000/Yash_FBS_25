# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacci_series():
    a=0
    b=1

    for i in range(1,n+1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
    return c

n = int(input("Enter the last number here : "))

res = fibonacci_series()

print(f'Fibonacci series upto {n} ')