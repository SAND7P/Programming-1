phone_book={}
user_details={}
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
while True:
    
    if name=="Stop":
        break
    user_details[name]=phone
print("phone book")