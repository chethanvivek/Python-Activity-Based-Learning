# Algorithm

1. Start.
2. Read the number of transactions.
3. If the number of transactions is less than or equal to zero:
   a. Display an invalid input message.
   b. Stop.
4. Create an empty list to store transaction IDs.
5. Repeat for the given number of transactions:
   a. Read a transaction ID.
   b. Convert the transaction ID to uppercase.
   c. Add the transaction ID to the list.
6. Create an empty list to store repeated transaction IDs.
7. Repeat through the transaction ID list:
   a. Count how many times the current ID appears.
   b. If the count is greater than one and the ID is not already in the repeated list, add it.
8. Display the total number of transactions.
9. If repeated transactions exist:
   a. Display each repeated transaction ID.
   b. Display its occurrence count.
   c. Display the number of repeated transaction IDs.
10. Otherwise, display that no repeated transactions were found.
11. Stop.
