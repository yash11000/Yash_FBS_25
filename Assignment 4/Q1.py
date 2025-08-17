# Q1 WAP to print all even numbers until n.
from itertools import count

n = int(input("Enter the number here : "))

for i in range (1,n+1):
    if i % 2 == 0:
        print(i,end=" ")
print(f'This are even numbers between 1 to {n}')