Item_name=input("Enter Item Name: ")
Item_price=int(input("Enter Item Price: "))
Quantity=int(input("Enter Quantity: "))
Sub_Total=Item_price*Quantity
GST=15/100*Sub_Total
Total=Sub_Total+GST
print("---------RECEIPT---------")
print("Item Name: ",Item_name)
print("Item Price: ",Item_price)
print("Quantity: ",Quantity)
print("Sub Total: ",Sub_Total)
print("GST (15%):  ",GST)
print("Total: ",Total)
print("----------------------------")

