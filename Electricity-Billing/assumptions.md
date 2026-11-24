# Assumptions – Progressive Electricity Billing

1. Electricity consumption is measured in units (kWh).
2. The electricity bill is calculated using progressive billing slabs:
   - First 100 units: ₹1.50 per unit.
   - Next 100 units (101–200): ₹2.50 per unit.
   - Above 200 units: ₹4.00 per unit.
3. A fixed charge of ₹50 is added to every monthly bill.
4. A rebate of 5% of energy charges is applied when monthly consumption is 100 units or less.
5. A surcharge of 5% of energy charges is applied when monthly consumption exceeds 200 units.
6. The rebate and surcharge are calculated on energy charges only, not on fixed charges.
7. Rebate and surcharge are not applied together in the same monthly bill.
8. The user enters electricity consumption for multiple months.
9. At least two months of consumption data are required for monthly comparison.
10. An increase of more than 30% in consumption compared with the previous month is considered unusual.
11. Negative electricity consumption and invalid numerical inputs are not accepted.
12. All tariff rates, fixed charges, rebate percentages, surcharge percentages, and unusual-increase thresholds are assumed to be predefined in the program.
13. These tariff values are sample values used for this assignment and do not represent actual electricity-board rates.
