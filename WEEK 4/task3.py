print("---------------------------")
scores=[65,72,80,55,90,68,77]
count=0
for score in scores:
    if score>70:
        count=count+1
print("Students scoring above 70 : ",count)
for score in scores:
    if score>=60:
        print(score,"pass")
    else:
        print(score,"fail")
print("---------------------------")