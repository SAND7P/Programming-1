class ShoppingCart:
    def __init__(self,customer_name,product_name,quantity,price):
        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.total=0
        self.discount=0
        self.total_after_discount=0

    def calculate_total_price(self):
        total = self.quantity * self.price
        self.total=total


    def apply_discount(self):
        if self.total >= 500:
            self.discount = self.total * 0.10
            self.total_after_discount = self.total-self.discount
        else:
            print("NO DISCOUNT")

    def display_cart(self):
        print("Customer Name:",self.customer_name)
        print("Product Name:",self.product_name)
        print("Quantity:",self.quantity)
        print("Price:",self.price)

        print("Total Price $:", self.total)
        print("Discount:",self.discount)
        print("Total After Discount:",self.total_after_discount)

    def update_quantity(self,quantity):
        self.quantity = +self.quantity+quantity
        print("Updated quantity:",self.quantity)
    def remove_item(self):
        self.quantity =0
        print("Items Removed from the cart")

cart1=ShoppingCart("ammar","hullu",5,100)
cart2=ShoppingCart("akbar","tullu",27,400)


print("=========CART 1==========")

cart1.calculate_total_price()
cart1.apply_discount()
cart1.display_cart()
cart1.update_quantity(4)
cart1.remove_item()

print("=========CART 2==========")

cart2.calculate_total_price()
cart2.apply_discount()
cart2.display_cart()
cart1.update_quantity(4)
cart1.remove_item()




