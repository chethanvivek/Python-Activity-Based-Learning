# Test Cases

## Test Case 1: Current Attendance is 60%

Input:

- Classes attended: 60
- Total classes: 100

Expected Output:

Current Attendance: 60.00%

| Future Attendance | Minimum Future Classes Required |
| ----------------- | ------------------------------: |
| 100%              |                              60 |
| 90%               |                             100 |
| 80%               |                             300 |

## Test Case 2: Current Attendance is 70%

Input:

- Classes attended: 70
- Total classes: 100

Expected Output:

Current Attendance: 70.00%

| Future Attendance | Minimum Future Classes Required |
| ----------------- | ------------------------------: |
| 100%              |                              20 |
| 90%               |                              36 |
| 80%               |                             100 |

## Test Case 3: Student is Already Eligible

Input:

- Classes attended: 80
- Total classes: 100

Expected Output:

Current Attendance: 80.00%

For all three scenarios:

- Student is already eligible.
- Additional classes required: 0.

## Test Case 4: Attendance is Exactly 75%

Input:

- Classes attended: 75
- Total classes: 100

Expected Output:

Current Attendance: 75.00%

For all three scenarios:

- Student is already eligible.
- Additional classes required: 0.

## Test Case 5: Invalid Attendance

Input:

- Classes attended: 110
- Total classes: 100

Expected Output:

Invalid attendance details

## Test Case 6: Invalid Total Classes

Input:

- Classes attended: 10
- Total classes: 0

Expected Output:

Invalid attendance details
