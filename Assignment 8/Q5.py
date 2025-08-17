# Sum of all prime numbers between 1 to n

# def odd_prime():
#     sum = 0
#     for i in range(2,n):
#         if i % (i//2+1) == 0 :
#             sum = sum + i
#         return sum
#
# n = int(input("Enter the last number here : "))
#
# res = odd_prime()
#
# print(res)


def checkprime():
    sum = 0
    for i in range(2,num//2+1):
        if (num % i == 0):
            sum = sum + i



num = int(input("Enter number : "))
res = checkprime()
print(res)
