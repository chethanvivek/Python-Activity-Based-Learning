BEGIN

    INPUT starting_weekday
    INPUT number_of_days

    IF starting_weekday < 1 OR starting_weekday > 7
       OR number_of_days < 28 OR number_of_days > 31 THEN

        DISPLAY "Invalid input"

    ELSE

        DISPLAY weekday headings

        SET current_day = 1
        SET first_week = TRUE

        WHILE current_day <= number_of_days

            FOR weekday FROM 1 TO 7

                IF first_week = TRUE AND weekday < starting_weekday THEN

                    DISPLAY blank space

                ELSE IF current_day <= number_of_days THEN

                    DISPLAY current_day
                    INCREMENT current_day by 1

                ELSE

                    DISPLAY blank space

                END IF

            END FOR

            MOVE to next calendar row
            SET first_week = FALSE

        END WHILE

    END IF

END
