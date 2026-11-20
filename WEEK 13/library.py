class Library:
    def __init__(self):
        self.books=[]
        self.borrows=[]
        self.book_id=1

    def book_register(self):
        title=input("Enter book title: ")
        for book in self.books:
            if title.lower() == book["Title"].lower():
                print("Book already registered.")

        author = input("Enter Book Author: ")
        available=input("Enter available copies: ")
        book = {
            "ID": "B" + str(self.book_id),
            "Title": title.lower(),
            "Author": author,
            "Copies": available,
        }

        self.books.append(book)

        print("Book registered successfully.")
        print("Book ID:", book["ID"])

        self.book_id += 1

        product = {"Title": self.books, "Author": author, "Available": available}
        self.books.append(product)
        self.book_id=+1

    def view_books(self):
            if len(self.books) == 0:
                print("Book Not Registered.")
                return

            for book in self.books:
                print("Book ID:", book["ID"])
                print("Book Title:", book["Title"])
                print("Book Author:", book["author"])
                print("Available Copies:", book["available"])

    def update_copies(self):
        book_id = input("Enter Book ID you want to update: ")

        for book in self.books:
            if book["ID"].lower() == book_id.lower():
                quantity = input("Enter new available copies: ")

                book["Copies"] = quantity

                print("Book", book["Title"], "has been updated to",
                      quantity, "copies.")
                return

        print("Book not found.")





