#BSCIT-01-0031/2026
#create an inventory dictionary
inventory = {
    "sugar":50,
    "rice":100,
    "flour":80,
    "salt":20,
}

#display the quantity of a specified product
print("quantity of rice:", inventory["rice"])

#add a new product
inventory["milk"] = 60

#update the quantity of an existing product
inventory["sugar"] = 70

#remove one product
del inventory["salt"]

#display the final inventory
print("\nfinal inventory:")

for product, quantity in inventory.items():
    print(product, ":", quantity)
