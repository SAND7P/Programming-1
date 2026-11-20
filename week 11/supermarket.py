class Store:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product : ", self.name)
        print("Price :", self.price)
        print("Quantity :", self.quantity)

    def add_item(self, amount):
        self.quantity = self.quantity + amount

    def remove_item(self, amount):
        self.quantity = self.quantity - amount
        if amount<=self.quantity:
            self.quantity = self.quantity - amount
        else:
            print("Sorry, you can't remove item")

    def calculate_total_price(self):
        total_price = self.price * self.quantity
        return total_price
#What is the name of our class?
#= The name of our class is store

#Is name an attribute or a method?
#= Name is an attribute

#Why are we using self.name?
#= We are using self.name to store the information of various instances

#What is the purpose of __init__( )?
#= The purpose of__init__() is to initialize the instances.

bread = Store('bread', 100, 10)
milk=Store('milk', 100, 10)
apple = Store('apple', 100, 10)
print("============STORE=============")
bread.display_info()
print("-------------------------")
milk.display_info()
print("-------------------------")
apple.display_info()
print("-------------------------")
milk.add_item(5)
milk.display_info()
bread.remove_item(5)
bread.display_info()
total1=milk.calculate_total_price()
total2=bread.calculate_total_price()
total3=apple.calculate_total_price()

grand_total=total1+total2+total3
print(grand_total)






