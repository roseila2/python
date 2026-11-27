#BSCIT-01-0031/2026
#supermarket discount calculation program
purchase_amount = input("enter the total purchase amount (ksh):")

purchase_amount = float(purchase_amount)

if purchase_amount >=10000:
    discount = 0.15 * purchase_amount
else:
    discount = 0.0

final_amount = purchase_amount - discount

print("\n---- purchase summary ----")
print(f"purchase amount : ksh {purchase_amount:.2f}")
print(f"discount :ksh {discount:.2f}")
print(f"final amount : ksh {final_amount:.2f}")
