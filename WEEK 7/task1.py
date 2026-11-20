#Functions to calculate average marks and display PASS/FAIL
def student_result(*marks):
    total=0
    for mark in marks:
        total = total + mark

        #Calculate Total marks
        average = total/len(marks)

        #Display average
        print("Average:",average)

        #Check pass or fail
        if average>=50:
            print("PASS")
        else:
            print("FAIL")

#MAIN PROGRAM
student_result(40,25,35,60,35)
student_result(70,75,65,50,)
student_result(30,25,35,60,)