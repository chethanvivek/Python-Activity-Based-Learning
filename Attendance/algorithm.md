# Algorithm

1. Start.
2. Set the eligibility threshold to 75%.
3. Read the number of classes attended.
4. Read the total number of classes conducted.
5. Check whether the input values are valid:
   - Classes attended must not be negative.
   - Total classes must be greater than zero.
   - Classes attended must not exceed total classes.
6. If the values are invalid, display an error message and stop.
7. Calculate the current attendance percentage:

   Current Attendance = (Classes Attended / Total Classes) \* 100

8. Display the current attendance percentage.
9. Define three future attendance scenarios: 100%, 90%, and 80%.
10. For each scenario:
    - Set future classes to zero.
    - If current attendance is already at least 75%, display zero
      additional classes required.
    - Otherwise, check whether the scenario percentage is greater
      than 75%.
    - If it is not greater, display that eligibility cannot be reached.
    - If it is greater, increase the number of future classes one
      at a time.
    - Calculate future attended classes by multiplying future classes
      by the scenario percentage and rounding down.
    - Calculate the new attendance percentage.
    - Continue until the new attendance percentage reaches 75%.
    - Display the minimum future classes required.
11. Stop.
