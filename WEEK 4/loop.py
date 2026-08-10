Item_no=int(input("Enter numbers of items purchased:"))
subtotal=0
for i in range(Item_no):
    name=input("Enter item name:")
    price=float(input("Enter price:"))
    quantity=int(input("Enter quantity:"))
    total=price*quantity
    print("Total price:",total)
    subtotal=subtotal+total

    print("--------------------------")
    print("Items num:",Item_no)
    print("price:",price)
    print("quantity:",quantity)
    print("--------------------------")
print("--------------------------")
print("subtotal:",subtotal)
print("--------------------------")
