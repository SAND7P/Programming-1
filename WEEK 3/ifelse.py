#Capture the students marks
m1=float(input("enter the first mark: "))
m2=float(input("enter the second mark: "))
m3=float(input("enter the third mark: "))
m4=float(input("enter the fourth mark: "))
grade=m1+m2+m3+m4/4
print("Grade :",grade)
if grade<50:
    print("FAIL-TRY AGAIN")
else:
    print("PASS,CONGRATULATION YOU GOT IT")

