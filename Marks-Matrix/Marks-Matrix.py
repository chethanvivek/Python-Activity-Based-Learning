print("STUDENT MARKS MATRIX ANALYSIS")

number_of_students = 3
number_of_subjects = 3

marks_matrix = []
valid = True

for student in range(1, number_of_students + 1):

    print("\nStudent", student)

    student_marks = []

    for subject in range(1, number_of_subjects + 1):

        mark = float(input("Enter marks for Subject " + str(subject) + ": "))

        if mark < 0 or mark > 100:

            print("Invalid marks. Marks must be between 0 and 100.")
            valid = False
            break

        student_marks.append(mark)

    if not valid:
        break

    marks_matrix.append(student_marks)


if valid:

    print("\n---------- STUDENT PERFORMANCE ----------")

    highest_total = -1
    top_student = 1

    for i in range(number_of_students):

        student_total = sum(marks_matrix[i])
        student_average = student_total / number_of_subjects

        print("Student", i + 1)
        print("Total Marks:", format(student_total, ".2f"))
        print("Average Marks:", format(student_average, ".2f"))

        if student_total > highest_total:

            highest_total = student_total
            top_student = i + 1

    print("\n---------- SUBJECT PERFORMANCE ----------")

    for j in range(number_of_subjects):

        subject_total = 0

        for i in range(number_of_students):

            subject_total = subject_total + marks_matrix[i][j]

        subject_average = subject_total / number_of_students

        print("Subject", j + 1)
        print("Average Marks:", format(subject_average, ".2f"))

        if subject_average < 40:

            print("Status: Low Performance")

        else:

            print("Status: Satisfactory Performance")

    print("\n---------- FINAL SUMMARY ----------")

    print("Top Performing Student:", top_student)
    print("Highest Total Marks:", format(highest_total, ".2f"))

    print("----------------------------------")