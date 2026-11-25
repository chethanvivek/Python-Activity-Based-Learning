print("ATTENDANCE RECOVERY COMPUTATION")

eligibility_threshold = 75

classes_attended = int(input("Enter classes attended: "))
total_classes = int(input("Enter total classes conducted: "))

if classes_attended < 0 or total_classes <= 0 or classes_attended > total_classes:

    print("Invalid attendance details")

else:

    current_attendance = (classes_attended / total_classes) * 100

    print("\nCurrent Attendance:", format(current_attendance, ".2f"), "%")
    print("Eligibility Threshold:", eligibility_threshold, "%")

    scenarios = [100, 90, 80]

    print("\n---------- FUTURE ATTENDANCE SCENARIOS ----------")

    for scenario in scenarios:

        print("\nFuture Attendance Scenario:", scenario, "%")

        if current_attendance >= eligibility_threshold:

            print("You are already eligible.")
            print("Additional classes required: 0")

        elif scenario <= eligibility_threshold:

            print("Eligibility cannot be reached under this scenario.")

        else:

            future_classes = 0
            new_attendance = current_attendance

            while new_attendance < eligibility_threshold:

                future_classes = future_classes + 1

                future_attended = int(future_classes * scenario / 100)

                new_attendance = (
                    (classes_attended + future_attended)
                    / (total_classes + future_classes)
                ) * 100

            print("Minimum future classes required:", future_classes)
            print("Attendance after these classes:",
                  format(new_attendance, ".2f"), "%")

    print("\n-------------------------------------------------")