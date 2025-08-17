# Q13 Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit = int(input("Enter the units of this month : "))

if(unit < 51):
    amt = unit * 0.50
    additional_charge = amt * 0.2
    final_amt = amt + additional_charge
elif(unit < 151):
    amt = unit * 0.75
    additional_charge = amt * 0.2
    final_amt = amt + additional_charge
elif(unit < 251):
    amt = unit * 1.20
    additional_charge = amt * 0.2
    final_amt = amt + additional_charge
elif(unit > 250):
    amt = unit * 1.50
    additional_charge = amt * 0.2
    final_amt = amt + additional_charge

print(f'Your total electricity bill of this month as per units is : {final_amt}')