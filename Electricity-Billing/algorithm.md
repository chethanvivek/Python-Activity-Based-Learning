# Algorithm – Progressive Electricity Billing

1. Start the program.

2. Define the following values:
   - First slab rate = ₹1.50 per unit.
   - Second slab rate = ₹2.50 per unit.
   - Third slab rate = ₹4.00 per unit.
   - Fixed charge = ₹50.
   - Rebate rate = 5%.
   - Surcharge rate = 5%.
   - Unusual increase threshold = 30%.

3. Ask the user to enter the number of months. Accept at least 2 months.

4. Create two empty lists:
   - One list to store monthly electricity consumption.
   - Another list to store monthly electricity bills.

5. Repeat the following steps for each month:

   a. Accept electricity units consumed for that month.

   b. Check whether the entered consumption is valid and non-negative.

   c. Calculate energy charges using progressive slabs:
   - If units are 100 or less, calculate all units at ₹1.50 per unit.
   - If units are between 101 and 200, calculate the first 100 units at ₹1.50 and the remaining units at ₹2.50.
   - If units are above 200, calculate the first 100 units at ₹1.50, the next 100 units at ₹2.50, and the remaining units at ₹4.00.

   d. Add the fixed charge of ₹50.

   e. If consumption is 100 units or less, calculate a 5% rebate on energy charges.

   f. If consumption is above 200 units, calculate a 5% surcharge on energy charges.

   g. Calculate the final bill by adding the fixed charge and surcharge, then subtracting the rebate from the energy charges.

   h. Store the monthly consumption and final bill in their respective lists.

   i. Display the billing details for that month.

6. Compare the consumption of each month with the previous month:

   a. Calculate the percentage increase in consumption.

   b. If the previous month's consumption is zero:
   - If the current month's consumption is greater than zero, identify it as an unusual increase.
   - If both months have zero consumption, consider the increase as 0%.

   c. If the percentage increase is greater than 30%, identify it as an unusual increase. Otherwise, identify it as a normal increase.

7. Find the month with the highest electricity consumption.

8. Find the month with the highest electricity bill.

9. Display the monthly comparison report, highest consumption, and highest electricity bill.

10. Stop the program.
