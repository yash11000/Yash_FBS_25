# Q10 Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

age = int(input("Enter the age of person : "))
gander = input("Enter the gander (Capitals latter only M/F) : ")

if (age >=21 and gander == 'M') or (age >=18 and gander == 'F' ):
    print("You are eligible for marry")
else:
    print("You are not eligible for marry")