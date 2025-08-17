# Sum of all odd numbers between 1 to n

def odd_sum():
    sum = 0
    for i in range(1,n):
        if i % 2 != 0:
            sum = sum + i
    return sum
n = int(input("Enter the last number here : "))

res = odd_sum()

print(res)