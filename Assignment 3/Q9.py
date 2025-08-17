# Q9 Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input("Enter the sub1 marks here"))
sub2 = int(input("Enter the sub2 marks here"))
sub3 = int(input("Enter the sub3 marks here"))
sub4 = int(input("Enter the sub4 marks here"))
sub5 = int(input("Enter the sub5 marks here"))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

if (total_marks >= 450):
    print("Congratulations you got A Grade")
elif (total_marks >= 350):
    print("Congratulations you got B Grade")
elif (total_marks >= 250):
    print("Congratulations you got C Grade")
else:
    print("Sorry you  are failed")