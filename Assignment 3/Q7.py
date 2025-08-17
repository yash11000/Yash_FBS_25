# Q7 Write a program to check if user has entered correct userid and password.

id = input("Enter the user ID here : ")
passwoed = int(input("Enter the pssword here : "))

if (id =='yash' and passwoed == 1234):
    print("You are valid for login")
else:
    print("You are not valid for login")