# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def digit_count(num):
    return len(str(num))
def armstrong_number(num):
    power = digit_count(num)
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10
    return total

def armstrong(num):
    return num == armstrong_number(num)

num = int(input("Enter the number here : "))

res = digit_count(num)
print('Number is',res,'digit number')
print('and')

if armstrong(num):
    print(num,'is armstrong number')
else:
    print(num,'is not an armstrong number')