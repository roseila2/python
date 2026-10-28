# BSCIT-01-0031/2026
class Book:
    # i & ii. Constructor to initialize attributes
    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    # iii. Method to calculate stock value
    def calculate_stock_value(self):
        stock_value = self.price * self.copies
        return stock_value

    # iv. Method to check stock status
    def check_stock(self):
        if self.copies > 0:
            return "In Stock"
        else:
            return "Out of Stock"


# v. Create two book objects and display their details
book1 = Book("Python Basics", "John Simiyu", 1200, 5)
book2 = Book("Database Systems", "Mary Mueni", 2500, 0)

print("--- Book 1 Details ---")
print(f"Title: {book1.title}")
print(f"Author: {book1.author}")
print(f"Total Stock Value: KSh {book1.calculate_stock_value():,.2f}")
print(f"Availability Status: {book1.check_stock()}\n")

print("--- Book 2 Details ---")
print(f"Title: {book2.title}")
print(f"Author: {book2.author}")
print(f"Total Stock Value: KSh {book2.calculate_stock_value():,.2f}")
print(f"Availability Status: {book2.check_stock()}")
