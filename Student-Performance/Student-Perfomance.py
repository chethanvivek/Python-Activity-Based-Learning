print("STUDENT PERFORMANCE TREND ANALYSIS")

number_of_subjects = 3
overall_total = 0
subject_averages = []
valid = True

for subject in range(1, number_of_subjects + 1):

    print("\nSubject", subject)

    marks = []

    for exam in range(1, 4):

        mark = float(input("Enter marks for Examination " + str(exam) + ": "))

        if mark < 0 or mark > 100:

            print("Invalid marks. Marks must be between 0 and 100.")
            valid = False
            break

        marks.append(mark)

    if not valid:
        break

    subject_average = sum(marks) / 3

    subject_averages.append(subject_average)
    overall_total = overall_total + subject_average

    print("Average Marks:", format(subject_average, ".2f"))

    if marks[2] > marks[0]:
        print("Performance Trend: Improved")

    elif marks[2] < marks[0]:
        print("Performance Trend: Declined")

    else:
        print("Performance Trend: No Change")

    if subject_average < 40:
        print("Status: Consistently Weak Subject")

    else:
        print("Status: Not a Weak Subject")


if valid:

    overall_average = overall_total / number_of_subjects

    print("\n---------- PERFORMANCE SUMMARY ----------")

    print("Overall Average:", format(overall_average, ".2f"))

    if overall_average >= 75:
        print("Performance Classification: Excellent")

    elif overall_average >= 60:
        print("Performance Classification: Good")

    elif overall_average >= 40:
        print("Performance Classification: Average")

    else:
        print("Performance Classification: Needs Improvement")

    print("-----------------------------------------")