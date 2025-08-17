# Write a program find reverse of a number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10      # get last digit
        rev = rev * 10 + digit
        num = num // 10       # remove last digit
    return rev

num = int(input("Enter a number: "))
print("Reverse of the number is:", reverse_number(num))
