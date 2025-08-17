# Q8 Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

user_id = input("Enter your user ID here : ")
password = int(input("Enter your password here : "))

import random

captcha = random.randint(1111, 9999)

print(f'Your captcha : {captcha}')

enter_captcha = input("Enter the above captcha here")

if(enter_captcha == str(captcha) and user_id == 'yash' and password == 1234):
    print("Please login")
elif(enter_captcha != str(captcha)):
    print("Please Enter the correct captcha ")
else:
    print("you are Not allowed for login ")