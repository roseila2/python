# BSCIT-01-0031/2026  MAINA ROSE WANGARI
# Accept inputs from customer
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity_input = input("Enter quantity purchased: ")
price_input = input("Enter price per item: ")

# Convert quantity to int and price to float
quantity = int(quantity_input)
price = float(price_input)

# Total Cost = Quantity × Price (Calculates total amount owed based on unit price and quantity)
total_cost = quantity * price

# Display purchase summary
print(f"\n--- Supermarket Purchase Summary ---")
print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price per Item: ${price:.3f}")
print(f"Total Cost: ${total_cost:.3f}")
