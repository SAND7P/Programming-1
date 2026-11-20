
print("-----------------------")
def check_result(mark   ):
    if mark >= 60:
        print(mark,"PASS")
    else:
        print(mark,"FAIL")
marks=[55,70,62,40,90]
#Call the function for each mark
for mark in marks:
    check_result(mark)
print("-----------------------")