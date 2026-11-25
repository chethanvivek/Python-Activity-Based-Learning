print("NESTED LOOP CALENDAR GENERATOR")

starting_weekday = int(input("Enter starting weekday (1-Sunday to 7-Saturday): "))
number_of_days = int(input("Enter number of days in the month: "))

if starting_weekday < 1 or starting_weekday > 7 or number_of_days < 28 or number_of_days > 31:

    print("Invalid input")

else:

    print("\nSun\tMon\tTue\tWed\tThu\tFri\tSat")

    current_day = 1
    first_week = True

    while current_day <= number_of_days:

        for weekday in range(1, 8):

            if first_week and weekday < starting_weekday:

                print("  ", end="\t")

            elif current_day <= number_of_days:

                print(format(current_day, "2d"), end="\t")
                current_day = current_day + 1

            else:

                print("  ", end="\t")

        print()
        first_week = False