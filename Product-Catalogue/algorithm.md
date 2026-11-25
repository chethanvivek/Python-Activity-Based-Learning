# Algorithm

1. Start.
2. Set the number of products to 3.
3. Create an empty list to store product records.
4. Repeat for each of the 3 products:
   a. Read the product ID.
   b. Read the product price.
   c. Read the stock quantity.
   d. Store the details as a tuple in the list.
5. Initialize total inventory value, invalid record count, and replenishment count to zero.
6. Repeat for each product tuple:
   a. Check whether the price is less than or equal to zero or stock quantity is negative.
   b. If invalid:
   - Display an invalid record message.
   - Increase the invalid record count.
     c. Otherwise:
   - Calculate inventory value using price × stock quantity.
   - Add the inventory value to the total.
   - If stock quantity is 5 or less, identify the product for replenishment.
7. Display the total inventory value.
8. Display the number of invalid records.
9. Display the number of products requiring replenishment.
10. Stop.
