seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Line 7 fix: use >, not =, and drop the redundant pre-assignment
overstock_risk = seasonal and current_stock > high_stock_threshold

# Line 9 is already correct; drop the redundant True on line 8
discount_eligible = not selling_well and not on_sale

# Line 11 is correct; drop the redundant True on line 10
make_discount = overstock_risk or discount_eligible

print("Should the item be discounted?", make_discount)