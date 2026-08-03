#Capture the students marks
m1=float(input("enter the first mark: "))
m2=float(input("enter the second mark: "))
m3=float(input("enter the third mark: "))
m4=float(input("enter the fourth mark: "))
grade=m1+m2+m3+m4/4
#average: 85-A, 70-B, 60-C, less than 60-Fail
print("Grade :",grade)
if grade>=85:
    print("A")
elif grade>=70:
    print("B")
elif grade>=60:
    print("C")
else:
    print("FAIL")