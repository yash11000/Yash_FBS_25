# #Q11 Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

ticket_amt = int(input("Enter the ticket amount : "))

age1 = int(input("Enter the first person age : "))

if (age1 < 12):
    dis_amt = ticket_amt * 0.3
    amt1 = ticket_amt - dis_amt
elif (age1 > 59):
    dis_amt = ticket_amt * 0.5
    amt1 = ticket_amt - dis_amt
else:
    amt1 = ticket_amt

age2 = int(input("Enter the second person age : "))


if (age2 < 12):
    dis_amt = ticket_amt * 0.3
    amt2 = ticket_amt - dis_amt
elif (age2 > 59):
    dis_amt = ticket_amt * 0.5
    amt2 = ticket_amt - dis_amt
else:
    amt2 = ticket_amt

age3 = int(input("Enter the third person age : "))

if (age3 < 12):
    dis_amt = ticket_amt * 0.3
    amt3 = ticket_amt - dis_amt
elif (age3 > 59):
    dis_amt = ticket_amt * 0.5
    amt3 = ticket_amt - dis_amt
else:
    amt3 = ticket_amt

age4 = int(input("Enter the fourth person age : "))

if (age4 < 12):
    dis_amt = ticket_amt * 0.3
    amt4 = ticket_amt - dis_amt
elif (age4 > 59):
    dis_amt = ticket_amt * 0.5
    amt4 = ticket_amt - dis_amt
else:
    amt4 = ticket_amt

age5 = int(input("Enter the fifth person age : "))

if (age5 < 12):
    dis_amt = ticket_amt * 0.3
    amt5 = ticket_amt - dis_amt
elif (age5 > 59):
    dis_amt = ticket_amt * 0.5
    amt5 = ticket_amt - dis_amt
else:
    amt5 = ticket_amt

total_amt = amt1 + amt2 + amt3 + amt4 + amt5

print(f'please pay : {total_amt}')