# Test Cases

## Test Case 1: Normal Product Catalogue Audit

**Input and Expected Output:**

```text
TUPLE-BASED PRODUCT CATALOGUE AUDIT

Product 1
Enter product ID: P101
Enter product price: 100
Enter stock quantity: 10

Product 2
Enter product ID: P102
Enter product price: 250
Enter stock quantity: 3

Product 3
Enter product ID: P103
Enter product price: 50
Enter stock quantity: 0

---------- PRODUCT CATALOGUE AUDIT ----------

Product ID: P101
Inventory Value: ₹ 1000.00
Status: Stock Sufficient

Product ID: P102
Inventory Value: ₹ 750.00
Status: Replenishment Required

Product ID: P103
Inventory Value: ₹ 0.00
Status: Replenishment Required

---------- AUDIT SUMMARY ----------
Total Products: 3
Invalid Records: 0
Products Requiring Replenishment: 2
Total Inventory Value: ₹ 1750.00
-----------------------------------
```

# Test Case 2: Invalid Product Records

TUPLE-BASED PRODUCT CATALOGUE AUDIT

Product 1
Enter product ID: P301
Enter product price: -100
Enter stock quantity: 10

Product 2
Enter product ID: P302
Enter product price: 200
Enter stock quantity: -2

Product 3
Enter product ID: P303
Enter product price: 50
Enter stock quantity: 4

---------- PRODUCT CATALOGUE AUDIT ----------

Product ID: P301
Invalid Product Record

Product ID: P302
Invalid Product Record

Product ID: P303
Inventory Value: ₹ 200.00
Status: Replenishment Required

---------- AUDIT SUMMARY ----------
Total Products: 3
Invalid Records: 2
Products Requiring Replenishment: 1
Total Inventory Value: ₹ 200.00

---
