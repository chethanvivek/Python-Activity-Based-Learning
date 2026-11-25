# Test Cases

## Test Case 1: Normal Student Marks Analysis

**Input:**

| Student   | Subject 1 | Subject 2 | Subject 3 |
| --------- | --------: | --------: | --------: |
| Student 1 |        80 |        70 |        90 |
| Student 2 |        60 |        20 |        40 |
| Student 3 |        30 |        20 |        25 |

**Expected Output:**

Student-wise performance:

| Student   | Total | Average |
| --------- | ----: | ------: |
| Student 1 |   240 |   80.00 |
| Student 2 |   120 |   40.00 |
| Student 3 |    75 |   25.00 |

Subject-wise averages:

| Subject   | Average | Status          |
| --------- | ------: | --------------- |
| Subject 1 |   56.67 | Satisfactory    |
| Subject 2 |   36.67 | Low Performance |
| Subject 3 |   51.67 | Satisfactory    |

Top Performing Student: 1

Highest Total Marks: 240.00

## Test Case 2: Invalid Marks

**Input:**

Student 1:

- Subject 1: 80
- Subject 2: 105

**Expected Output:**

Invalid marks. Marks must be between 0 and 100.

The program stops without displaying the final performance summary.
