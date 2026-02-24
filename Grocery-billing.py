# Grocery Store Billing System

total_amount = 0

for i in range(1, 6):
    price = float(input("Enter price of item {i}: "))
    quantity = int(input("Enter number of units for item {i}: "))
    
    item_cost = price * quantity
    total_amount += item_cost

print("\nOriginal Total Amount: Rs.", total_amount)

# Initialize discount
discount = 0

# Apply 10% discount if total exceeds Rs. 100
if total_amount > 100:
    discount = total_amount * 0.10
    final_amount = total_amount - discount
else:
    final_amount = total_amount

# Display discount and final payable amount
print("Discount Applied: Rs.", discount)

print("Final Payable Amount: Rs.", final_amount)
