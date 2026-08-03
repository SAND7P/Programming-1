PIN=1234
ACC_BALANCE=1000
print("---------------ATM-------------")
print("         Insert ATM CARD")
pin=float(input("Enter your PIN: "))
if pin!=PIN:
    print("Invalid PIN")
    print("--------------------------")
    exit()
elif pin==PIN:
    amt=float(input("Enter withdrawal Amount: "))
    if amt<=ACC_BALANCE:
        print("insufficient balance")
    else:
        print("Dispensing Amount ",amt)
        print("printing receipt")
        print("Please take your card")
print("--------------------------")
