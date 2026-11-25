# Test Cases

## Test Case 1: Multiple Repeated Transactions

**Input:**

Number of transactions: 4

| Transaction Number | Transaction ID |
| ------------------ | -------------- |
| 1                  | TX101          |
| 2                  | TX102          |
| 3                  | TX103          |
| 4                  | TX104         |


**Expected Output:**

```text
---------- TRANSACTION SUMMARY ----------
Total Transactions: 4
No repeated transactions found
-----------------------------------------
```
## Test Case 1: Multiple Repeated Transactions

**Input:**

Number of transactions: 2

| Transaction Number | Transaction ID |
| ------------------ | -------------- |
| 1                  | TX101          |
| 2                  | TX102          |

**Expected Output:**

```text
---------- TRANSACTION SUMMARY ----------
Total Transactions: 2
No repeated transactions found
-----------------------------------------
```
