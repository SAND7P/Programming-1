Monthly_Income=float(input("Enter your monthly income: "))
Rent=float(input("Enter your monthly rent amount: "))
Transport_Cost=float(input("Enter your monthly transportation cost: "))
Food_cost=float(input("Enter your monthly food cost: "))
Entertainment_cost=float(input("Enter your monthly entertainment cost: "))
Total_expenses=Rent+Transport_Cost+Food_cost+Entertainment_cost
Remaining_balance=Monthly_Income-Total_expenses
print("----Monthly Budget calculator------")
print("Total Expenses:",Total_expenses)
print("Remaining Balance:",Remaining_balance)
print("-----------------------")


