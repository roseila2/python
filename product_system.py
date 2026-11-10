#BSCIT-01-0031/2026
# Create Product class
class Product:

    # Method to assign product details
    def setProductDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    # Method to calculate stock value
    def calculateStockValue(self):
        self.stock_value = self.price * self.quantity
        return self.stock_value

    # Method to display product details
    def displayProductDetails(self):
        print("\n--- Product Details ---")
        print("Product Name:", self.name)
        print("Product Code:", self.code)
        print("Price: KSh", self.price)
        print("Quantity:", self.quantity)
        print("Stock Value: KSh", self.stock_value)


# Main section
product1 = Product()

product1.setProductDetails(
    "Laptop",
    "PRD101",
    50000,
    10
)

product1.calculateStockValue()

product1.displayProductDetails()
    
