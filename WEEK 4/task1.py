score=int(input("Enter your score :"))
while 100<score or score<0:
   print("Your score is Invalid")
   score=int(input("Enter your score :"))
if score>=80:
    print("Grade: A")
elif score>=60:
    print("Grade: B")
elif score>=50:
    print("Grade: C")
else:
    print("FAIL!!!!!")

