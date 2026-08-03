c1fm=float(input("Enter final marks of course 1: "))
c2fm=float(input("Enter final marks of course 2: "))
c3fm=float(input("Enter final marks of course 3: "))
c4fm=float(input("Enter final marks of course 4: "))
average=(c1fm+c2fm+c3fm+c4fm)/4
print("-------STUDENT RESULT--------")
print("Course1:",c1fm)
print("Course2:",c2fm)
print("Course3:",c3fm)
print("Course4:",c4fm)
print("Average marks obtained: ",average)
if average>=85:
    print("GRADE: A,Remark: Excellent ",average)
elif average>=75:
   print("GRADE: B,Remark: Very Good",average)
elif average>=65:
    print("GRADE: C,Remark: Good",average)
elif average>=50:
    print("GRADE: D,Remark: Pass",average)
else:
    print("GRADE: F,Remark: Fail",average)
print("--------------------------")