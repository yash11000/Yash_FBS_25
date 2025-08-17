# Q5 WAP to print Fibonacci series upto n.

n = int(input("Enter the number here : "))

a = 0
b= 1

for i in range (0,n):
    c = a + b
    print(c)
    a = b
    b = c