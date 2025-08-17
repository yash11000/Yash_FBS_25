#Q2 WAP to print all odd numbers until n.

n = int(input("Enter the number here : "))

for i in range (1,n+1):
    if i % 2 != 0:
        print(i,end=" ")
print(f'This are odd numbers between 1 to {n}')