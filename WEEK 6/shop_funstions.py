def get_items():
    items={}

    while True:
        item_name = input("Enter item name: ")
        if item_name.lower()== "done":
           break
        if item_name.lower()!= "done":
            price = float(input("Enter price: "))
            items[item_name] = price

    return items
def print_items(dict_items):
    print("Items:")
    total_price=0


    for item,price in dict_items.items():
        print(item,price)
        total_price=total_price+price
    print(total_price)
