# Q6 Write a program to calculate profit or loss.

costprice = int(input("Enter the cost  price of product : "))
sellingprice = int(input("Enter the selling price of product : "))

profit = sellingprice - costprice

if (profit > 0):
    print("You are in profit")
elif (profit == 0):
    print("You are not in loss or profit")
else:
    print("You are in loss")
print(profit)