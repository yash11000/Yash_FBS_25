# # Q12 Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter the three digit number here : "))

temp = num

d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

print(f'(D1)={d1} (D2)={d2} (D3) = {d3}')

new_num = (d1 * 100) + (d2 * 10) + d3

print(new_num)

