# Test Cases – Retail Billing with Multiple Discount Rules

Test Case 1: Bill below ₹500, non-member

Input:
Number of items = 2

Item 1:
Price = 100
Quantity = 2

Item 2:
Price = 100
Quantity = 1

Membership = no

Expected Output:
Subtotal = ₹300
Purchase Discount = ₹15
Membership Discount = ₹0
Final Payable Amount = ₹285

Test Case 2: Bill between ₹500 and ₹2500, non-member

Input:
Number of items = 2

Item 1:
Price = 500
Quantity = 2

Item 2:
Price = 200
Quantity = 1

Membership = no

Expected Output:
Subtotal = ₹1200
Purchase Discount = ₹120
Membership Discount = ₹0
Final Payable Amount = ₹1080

Test Case 3: Bill above ₹2500, non-member

Input:
Number of items = 2

Item 1:
Price = 1000
Quantity = 2

Item 2:
Price = 1000
Quantity = 1

Membership = no

Expected Output:
Subtotal = ₹3000
Purchase Discount = ₹450
Membership Discount = ₹0
Final Payable Amount = ₹2550

Test Case 4: Bill above ₹2500, member

Input:
Number of items = 2

Item 1:
Price = 1000
Quantity = 2

Item 2:
Price = 1000
Quantity = 1

Membership = yes

Expected Output:
Subtotal = ₹3000
Purchase Discount = ₹450
Amount After Purchase Discount = ₹2550
Membership Discount = ₹127.50
Final Payable Amount = ₹2422.50

Test Case 5: Invalid item quantity

Input:
Number of items = 1

Item 1:
Price = 500
Quantity = 0

Expected Output:
Invalid item details

Test Case 6: Invalid membership status

Input:
Number of items = 1

Item 1:
Price = 600
Quantity = 1

Membership = maybe

Expected Output:
Invalid membership status
