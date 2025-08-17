# Write a program to find sum of digits of a number.
def digit_sum(num):
    temp = num
    sum = 0
    while temp > 0 :
        d = temp % 10
        sum = sum + d
        temp = temp//10
        print(d)
    print('Sum of digits is', sum)

num = int(input("Enter the number here : "))

res = digit_sum(num)

print(res)