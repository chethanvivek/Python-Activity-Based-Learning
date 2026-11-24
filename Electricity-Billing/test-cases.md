# Test Cases – Progressive Electricity Billing

| Test Case | Number of Months | Monthly Consumption (Units) | Expected Result |
|---|---:|---|---|
| 1 | 3 | 100, 150, 250 | Bills: ₹192.50, ₹325.00, ₹680.00. Both increases are unusual. |
| 2 | 2 | 100, 110 | Bills: ₹192.50, ₹225.00. Increase of 10%, normal increase. |

## Detailed Test Case 1

**Input:**
- Number of months: 3
- Month 1: 100 units
- Month 2: 150 units
- Month 3: 250 units

**Expected Output:**
- Month 1 bill: ₹192.50
- Month 2 bill: ₹325.00
- Month 3 bill: ₹680.00

**Monthly Comparison:**
- Month 1 to Month 2: 50% – Unusual increase.
- Month 2 to Month 3: 66.67% – Unusual increase.

## Detailed Test Case 2

**Input:**
- Number of months: 2
- Month 1: 100 units
- Month 2: 110 units

**Expected Output:**
- Month 1 bill: ₹192.50
- Month 2 bill: ₹225.00

**Monthly Comparison:**
- Month 1 to Month 2: 10% – Normal increase.

## Conclusion

Both test cases verify electricity bill calculations, progressive slab rates, fixed charges, rebates, surcharges, and monthly consumption comparisons.