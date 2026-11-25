# Test Cases

## Test Case 1: Normal Performance Analysis

**Input:**

| Subject   | Exam 1 | Exam 2 | Exam 3 |
| --------- | -----: | -----: | -----: |
| Subject 1 |     60 |     70 |     80 |
| Subject 2 |     80 |     75 |     70 |
| Subject 3 |     30 |     35 |     35 |

**Expected Output:**

| Subject   | Average | Trend    | Status   |
| --------- | ------: | -------- | -------- |
| Subject 1 |   70.00 | Improved | Not Weak |
| Subject 2 |   75.00 | Declined | Not Weak |
| Subject 3 |   33.33 | Improved | Weak     |

Overall Average: 59.44

Performance Classification: Average

## Test Case 2: Excellent Performance

**Input:**

| Subject   | Exam 1 | Exam 2 | Exam 3 |
| --------- | -----: | -----: | -----: |
| Subject 1 |     80 |     85 |     90 |
| Subject 2 |     75 |     80 |     85 |
| Subject 3 |     90 |     90 |     90 |

**Expected Output:**

Overall Average: 85.00

Performance Classification: Excellent

## Test Case 3: Average Performance

**Input:**

| Subject   | Exam 1 | Exam 2 | Exam 3 |
| --------- | -----: | -----: | -----: |
| Subject 1 |     40 |     45 |     50 |
| Subject 2 |     50 |     50 |     50 |
| Subject 3 |     55 |     50 |     45 |

**Expected Output:**

Overall Average: 48.33

Performance Classification: Average

## Test Case 4: Needs Improvement

**Input:**

| Subject   | Exam 1 | Exam 2 | Exam 3 |
| --------- | -----: | -----: | -----: |
| Subject 1 |     20 |     25 |     30 |
| Subject 2 |     30 |     35 |     30 |
| Subject 3 |     35 |     30 |     25 |

**Expected Output:**

Overall Average: 28.33

Performance Classification: Needs Improvement

## Test Case 5: Invalid Marks

**Input:**

Subject 1:

- Examination 1: 80
- Examination 2: 105

**Expected Output:**

Invalid marks. Marks must be between 0 and 100.

The program stops without calculating the final performance summary.
