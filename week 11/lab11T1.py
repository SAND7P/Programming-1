class Book:
    def __init__(self,title,author,copies_available):
        self.title=title
        self.author=author
        self.copies_available=copies_available

    def display_book(self):
        print("Title: ", self.title)
        print("Author name: ", self.author)
        print("Number of copies available: ", self.copies_available)

    def borrow_book(self):
        if self.copies_available>0:
            self.copies_available=self.copies_available+1
            print("Book borrowed successfully")
        else:
            print("Out of stock")

    def return_book(self):
        self.copies_available=self.copies_available+1
        print("Book returned successfully")

book1=Book("CR&S","Himself",7)
book2=Book("LM10","Zeus",4)
book3=Book("NJR","Dinho",5)
print("=============BOOK1==============")
book1.display_book()
book1.borrow_book()
book1.return_book()
print("-----Updated Information-----")
book1.display_book()

print("=============BOOK1==============")
book2.display_book()
book2.borrow_book()
book2.return_book()
print("-----Updated Information-----")
book2.display_book()

print("=============BOOK1==============")
book3.display_book()
book3.borrow_book()
book3.return_book()
print("-----Updated Information-----")
book3.display_book()






