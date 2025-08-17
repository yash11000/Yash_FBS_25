# Q11 WAP to check if given number Strong Number.

num = int(input("Enter the number here : "))

temp = num
sum = 0

while (temp > 0):
    d = temp % 10
    temp = temp // 10

    i = 1
    fact = 1
    while ( i<=d):
        fact = fact * i
        i = i +1

    sum = sum + fact

if (sum == num):
    print(f'{num} This is the strong number')
else:
    print(f'{num} This is not a strong number')
