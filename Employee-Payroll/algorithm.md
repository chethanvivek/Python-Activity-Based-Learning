# Algorithm – Employee Payroll and Deduction Analysis

1. Start the program.

2. Input the employee's:
   - Basic pay
   - Allowances
   - Overtime hours
   - Overtime rate
   - Incentives

3. Check whether any input is negative.
   - If negative, display an error message.
   - Otherwise, continue.

4. Calculate overtime pay:
   Overtime Pay = Overtime Hours × Overtime Rate

5. Calculate gross salary:
   Gross Salary = Basic Pay + Allowances + Overtime Pay + Incentives

6. Calculate progressive deductions:
   - If gross salary is less than or equal to ₹10,000,
     deduction = 0.
   - If gross salary is between ₹10,000 and ₹20,000,
     apply 5% to the amount above ₹10,000.
   - If gross salary is above ₹20,000,
     apply 5% to the first ₹10,000 above ₹10,000
     and 10% to the amount above ₹20,000.

7. Calculate net salary:
   Net Salary = Gross Salary - Total Deductions

8. Display the salary statement containing:
   - Basic pay
   - Allowances
   - Overtime pay
   - Incentives
   - Gross salary
   - Total deductions
   - Net salary

9. Stop the program.
