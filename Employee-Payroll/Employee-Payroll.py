print("EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS")

basic_pay = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

if basic_pay < 0 or allowances < 0 or overtime_hours < 0 or overtime_rate < 0 or incentives < 0:
    print("Invalid input. Values cannot be negative.")

else:
    overtime_pay = overtime_hours * overtime_rate

    gross_salary = basic_pay + allowances + overtime_pay + incentives

    if gross_salary <= 10000:
        deduction = 0

    elif gross_salary <= 20000:
        deduction = (gross_salary - 10000) * 0.05

    else:
        deduction = (10000 * 0.05) + (gross_salary - 20000) * 0.10

    net_salary = gross_salary - deduction

    print("\n---------- SALARY STATEMENT ----------")
    print("Basic Pay       : ₹", format(basic_pay, ".2f"))
    print("Allowances      : ₹", format(allowances, ".2f"))
    print("Overtime Pay    : ₹", format(overtime_pay, ".2f"))
    print("Incentives      : ₹", format(incentives, ".2f"))
    print("--------------------------------------")
    print("Gross Salary    : ₹", format(gross_salary, ".2f"))
    print("Total Deductions: ₹", format(deduction, ".2f"))
    print("--------------------------------------")
    print("Net Salary      : ₹", format(net_salary, ".2f"))
    print("--------------------------------------")