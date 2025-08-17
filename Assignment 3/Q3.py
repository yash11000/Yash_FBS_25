# Q3 Write a program to input angles of a triangle and check whether triangle is valid or not.

ang1 = int(input("Enter the first angle of triangle : "))
ang2 = int(input("Enter the second angle of triangle : "))
ang3 = int(input("Enter the third angle of triangle : "))

if (ang1 + ang2 + ang3 == 180):
    print("This is a triangle")
else:
    print("This is not a triangle")