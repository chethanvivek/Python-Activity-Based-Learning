
# Progressive Electricity Billing

# Electricity slab rates
slab1_rate = 1.50
slab2_rate = 2.50
slab3_rate = 4.00

# Fixed charges and percentages
fixed_charge = 50
rebate_rate = 0.05
surcharge_rate = 0.05
threshold = 30

# Get number of months
number_of_months = int(input("Enter number of months: "))

# Validate number of months
while number_of_months < 2:
    print("Please enter at least 2 months.")
    number_of_months = int(input("Enter number of months: "))

# Create empty lists
consumption = []
bills = []

# Calculate electricity bill for each month
for i in range(number_of_months):

    print("\nMonth", i + 1)

    units = float(input("Enter units consumed: "))

    # Validate electricity consumption
    while units < 0:
        print("Invalid consumption. Enter non-negative units.")
        units = float(input("Enter units consumed: "))

    # Calculate energy charges using progressive slabs
    if units <= 100:
        energy_charge = units * slab1_rate

    elif units <= 200:
        energy_charge = (100 * slab1_rate) + ((units - 100) * slab2_rate)

    else:
        energy_charge = (100 * slab1_rate) + (100 * slab2_rate) + ((units - 200) * slab3_rate)

    # Initialize rebate and surcharge
    rebate = 0
    surcharge = 0

    # Calculate rebate or surcharge
    if units <= 100:
        rebate = energy_charge * rebate_rate

    elif units > 200:
        surcharge = energy_charge * surcharge_rate

    # Calculate final bill
    final_bill = energy_charge + fixed_charge + surcharge - rebate

    # Store consumption and bill
    consumption.append(units)
    bills.append(final_bill)

    # Display monthly billing details
    print("Units consumed:", units)
    print("Energy charges: Rs.", round(energy_charge, 2))
    print("Fixed charges: Rs.", fixed_charge)
    print("Rebate: Rs.", round(rebate, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Final bill: Rs.", round(final_bill, 2))


# Compare monthly consumption
print("\nMONTHLY COMPARISON")

for i in range(1, number_of_months):

    previous_units = consumption[i - 1]
    current_units = consumption[i]

    print("\nMonth", i, "to Month", i + 1)

    if previous_units == 0:

        if current_units > 0:
            print("Unusual increase!")

        else:
            print("0% change")
    
    else:
        percentage_increase = ((current_units - previous_units) / previous_units) * 100

        print("Percentage change:", round(percentage_increase, 2), "%")

        if percentage_increase > threshold:
            print("Unusual increase!")

        else:
            print("Normal increase.")


# Find highest consumption and highest bill
highest_consumption = max(consumption)
highest_bill = max(bills)

# Find the month numbers
consumption_month = consumption.index(highest_consumption) + 1
bill_month = bills.index(highest_bill) + 1

# Display final report
print("\nFINAL REPORT")

print("Highest consumption: Month", consumption_month, "-", highest_consumption, "units")

print("Highest bill: Month", bill_month, "- Rs.", round(highest_bill, 2))

print("\nProgram completed.")
