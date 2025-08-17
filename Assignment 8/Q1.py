# Write a program to calculate area of rectangle

def area(x,y):
    area_triangle = x * y
    print(f'Area of triangle is {area_triangle}')

x = int(input("Enter length of rectangle here : "))
y = int(input("Enter breadth of rectangle here : "))

area(x,y)