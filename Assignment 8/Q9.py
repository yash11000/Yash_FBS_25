# Write a program to check if entered number is a palindrome or not.

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10      # get last digit
        rev = rev * 10 + digit
        num = num // 10       # remove last digit
    return rev

num = int(input("Enter a number: "))

reverse_number(num)
if  (num == reverse_number(num)):
    print(f'{num} is a palindrome number')
else:
    print(f'{num} is not palindrome number')