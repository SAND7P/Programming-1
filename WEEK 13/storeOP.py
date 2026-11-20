class InventoryManagement:
    def __init__(self):
        self.productlist=[]
        self.salelist=[]
        self.producti_id=1

    def product_register(self):
        name=input("Enter product name: ")
        for product in self.productlist:
            if product["name"].lower() == name.lower():
                print("Product already exists")
                return
        price=float(input("Enter product price: "))
        stock=int(input("Enter product stock quantity: "))

        product={"ID":self.producti_id,"name":name,"price":price,"stock":stock}
        self.productlist.append(product)
        self.producti_id+=1

    def update_stock(self):
        product_id=int(input("Enter product ID for update: "))
        for product in self.productlist:
            if product["ID"] == product_id:
                quantity=int(input("Enter quantity for update: "))
                product["stock"]-=quantity
                print("Stock updated successfully",product["stock"])
                return

        print("Product ID does not exist")

    def sell_product(self):
        product_id=int(input("Enter product ID for sell: "))
        qunty_sale=int(input("Enter quantity for sell: "))

        for product in self.productlist:
            if product["ID"] == product_id:
                new_stock=product["stock"]-qunty_sale
                product["stock"]=new_stock

                total=qunty_sale*product["price"]
                sale={"ID":id,"Quantity":qunty_sale,"Total":total}
                self.salelist.append(sale)
                print("Product Sold successfully ",product["ID"])
                print("total price: ", total)
                return
            print("Product", {product["Name"]}, "not found.")

    def search_product(self):
        product_id = int(input("Enter ID for search: "))

        for product in self.productlist:
            if product["ID"] == product_id:
                print("Product ID: ", product["ID"])
                print("Product Name: ", product["name"])
                print("Product Price: ", product["price"])
                print("Product Stock quantity: ", product["stock"])
                return
        print("Product",{product["Name"]}, "not found.")

    def display_summary(self):
        total_products = len(self.productlist)
        item_sold = 0
        sales_value = 0

        for sale in self.salelist:
            item_sold += sale["Quantity"]
            sales_value += sale["Total"]

        print("---------------------Sales Summary----------------------")
        print("Total number of products: ", total_products)
        print("Total items sold : ", item_sold)
        print("Total sales value: ", sales_value)

        print("-----------------Current Stock levels--------------------")
        for product in self.productlist:
            print(product["Name"], "-Stock: ", product["Stock"])

    def menu_system(self):
        while True:
            print("-----------Store Operations-------------")
            print("1. Add Product")
            print("2. View All Product")
            print("3. Update Product stock")
            print("4. Sell product")
            print("5. Search product")
            print("6. View Sales Summary")
            print("7. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.product_register()
            elif choice == 2:
                self.search_product()
            elif choice == 3:
                self.update_stock()
            elif choice == 4:
                self.sell_product()
            elif choice == 5:
                self.search_product()
            elif choice == 6:
                self.display_summary()
            elif choice == 7:
                print("Thank you")
                break
            else:
                print("Please enter a valid choice.")

pro=InventoryManagement()
pro.menu_system()

