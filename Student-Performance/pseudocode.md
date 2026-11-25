### 6. `pseudocode.md`

```text
BEGIN

    SET number_of_subjects = 3
    SET overall_total = 0
    SET valid = TRUE

    FOR each subject from 1 to 3

        DISPLAY subject number
        CREATE empty list marks

        FOR exam from 1 to 3

            INPUT mark

            IF mark < 0 OR mark > 100 THEN
                DISPLAY "Invalid marks"
                SET valid = FALSE
                BREAK
            END IF

            ADD mark to marks

        END FOR

        IF valid = FALSE THEN
            BREAK
        END IF

        CALCULATE subject_average = SUM(marks) / 3
        ADD subject_average to overall_total

        DISPLAY subject_average

        IF third examination mark > first examination mark THEN
            DISPLAY "Improved"
        ELSE IF third examination mark < first examination mark THEN
            DISPLAY "Declined"
        ELSE
            DISPLAY "No Change"
        END IF

        IF subject_average < 40 THEN
            DISPLAY "Consistently Weak Subject"
        END IF

    END FOR

    IF valid = TRUE THEN

        CALCULATE overall_average = overall_total / 3

        IF overall_average >= 75 THEN
            SET classification = "Excellent"
        ELSE IF overall_average >= 60 THEN
            SET classification = "Good"
        ELSE IF overall_average >= 40 THEN
            SET classification = "Average"
        ELSE
            SET classification = "Needs Improvement"
        END IF

        DISPLAY overall_average
        DISPLAY classification

    END IF

END
```
