AssignmentMark=float(input("Enter Your Assignment Mark/100: "))
TestMark=float(input("Enter Your Test Mark/100: "))
ExamMark=float(input("Enter Your Exam Mark/100: "))
Ass_cot=AssignmentMark/100*30
Mrk_cot=TestMark/100*30
Exam_cot=ExamMark/100*40
print("------STUDENT RESULT-------")
print("Assignment Mark:",AssignmentMark)
print("Test Mark:",TestMark)
print("Exam Mark:",ExamMark)
print("Assignment Contribution:",Ass_cot)
print("Test Contribution:",Mrk_cot)
print("Exam Contribution:",Exam_cot)
Final_grade=Ass_cot+Mrk_cot+Exam_cot
print("Final Grade:",Final_grade)
print("-------------------")

