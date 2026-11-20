def print_results(students ):
    for name, marks in students.items():
        if marks>=60:
         print(name,marks,"PASS")
    else:
        print(name,marks,"FAIL")

students={
    "John":65,
    "Marry":82,
    "Ali":55,
    "Sina":99
}
print_results(students)