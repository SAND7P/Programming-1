acc_balance = 1500
amount=float(input("ENTER WITHDRAWAL AMT: "))

if amount >= acc_balance:
    print("INSUFFICIENT BALANCE")
else:
    print("DISPENSING-take your cash")
    new_balance = acc_balance - amount
    print("YOUR BALANCE NOW: ",new_balance)
    