# Algorithm – Retail Billing with Multiple Discount Rules

1. Start the program.

2. Input the number of items purchased.

3. Check whether the number of items is greater than zero.
   - If not, display an invalid input message.
   - Otherwise, continue.

4. Initialize subtotal to zero.

5. Repeat for each item:
   - Input item price.
   - Input item quantity.
   - Check whether the price and quantity are valid.
   - Calculate item total = price × quantity.
   - Add item total to subtotal.

6. Check the subtotal:
   - If subtotal is below ₹500, apply 5% discount.
   - If subtotal is between ₹500 and ₹2500, apply 10% discount.
   - If subtotal is ₹2500 or above, apply 15% discount.

7. Calculate the amount after purchase discount.

8. Ask whether the customer is a membership customer.

9. If the customer is a member:
   - Apply an additional 5% discount on the remaining amount.
     Otherwise:
   - Set membership discount to zero.

10. Calculate the final payable amount.

11. Display:
    - Subtotal
    - Purchase discount
    - Membership discount
    - Final payable amount

12. Stop the program.
