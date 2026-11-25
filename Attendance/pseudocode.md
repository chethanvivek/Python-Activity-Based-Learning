BEGIN

    SET eligibility_threshold = 75

    INPUT classes_attended
    INPUT total_classes

    IF classes_attended < 0 OR total_classes <= 0
       OR classes_attended > total_classes THEN

        DISPLAY "Invalid attendance details"

    ELSE

        current_attendance =
            (classes_attended / total_classes) * 100

        DISPLAY current_attendance

        SET scenarios = [100, 90, 80]

        FOR EACH scenario IN scenarios

            DISPLAY scenario

            IF current_attendance >= eligibility_threshold THEN

                DISPLAY "0 future classes required"

            ELSE IF scenario <= eligibility_threshold THEN

                DISPLAY "Eligibility cannot be reached"

            ELSE

                SET future_classes = 0
                SET new_attendance = current_attendance

                WHILE new_attendance < eligibility_threshold

                    INCREASE future_classes BY 1

                    future_attended =
                        INTEGER PART OF
                        (future_classes * scenario / 100)

                    new_attendance =
                        ((classes_attended + future_attended) /
                        (total_classes + future_classes)) * 100

                END WHILE

                DISPLAY future_classes

            END IF

        END FOR

    END IF

END
