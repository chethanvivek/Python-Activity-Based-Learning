BEGIN

    SET number_of_students = 3
    SET number_of_subjects = 3

    CREATE empty list marks_matrix
    SET valid = TRUE

    FOR student FROM 1 TO 3

        CREATE empty list student_marks

        FOR subject FROM 1 TO 3

            INPUT mark

            IF mark < 0 OR mark > 100 THEN
                DISPLAY "Invalid marks"
                SET valid = FALSE
                BREAK
            END IF

            ADD mark TO student_marks

        END FOR

        IF valid = FALSE THEN
            BREAK
        END IF

        ADD student_marks TO marks_matrix

    END FOR

    IF valid = TRUE THEN

        SET highest_total = -1
        SET top_student = 1

        FOR each student IN marks_matrix

            CALCULATE student_total
            CALCULATE student_average

            DISPLAY student_total and student_average

            IF student_total > highest_total THEN
                SET highest_total = student_total
                SET top_student = current student
            END IF

        END FOR

        FOR each subject

            CALCULATE subject_total
            CALCULATE subject_average

            DISPLAY subject_average

            IF subject_average < 40 THEN
                DISPLAY "Low Performance"
            END IF

        END FOR

        DISPLAY top_student

    END IF

END
