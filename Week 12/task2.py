def validate_lastname(lastname):
    lastname = input("Please enter your name: ")
    lastname = lastname.strip()
    if lastname == "":
        return False, "Name is required"
    if not lastname.isalpha():
        return False, "Name is required"
students = [
    ("John"),
    ("Michael")
]