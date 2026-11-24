# Pseudocode – Progressive Electricity Billing

```text
START

    SET slab1_rate = 1.50
    SET slab2_rate = 2.50
    SET slab3_rate = 4.00
    SET fixed_charge = 50
    SET rebate_rate = 5 / 100
    SET surcharge_rate = 5 / 100
    SET threshold = 30

    INPUT number_of_months

    CREATE empty list consumption
    CREATE empty list bills

    FOR each month from 1 to number_of_months

        INPUT units

        IF units < 0 THEN
            DISPLAY "Invalid consumption"
            REPEAT input
        END IF

        IF units <= 100 THEN
            energy_charge = units * slab1_rate

        ELSE IF units <= 200 THEN
            energy_charge = (100 * slab1_rate) +
                            ((units - 100) * slab2_rate)

        ELSE
            energy_charge = (100 * slab1_rate) +
                            (100 * slab2_rate) +
                            ((units - 200) * slab3_rate)
        END IF

        rebate = 0
        surcharge = 0

        IF units <= 100 THEN
            rebate = energy_charge * rebate_rate

        ELSE IF units > 200 THEN
            surcharge = energy_charge * surcharge_rate
        END IF

        final_bill = energy_charge + fixed_charge +
                     surcharge - rebate

        ADD units TO consumption
        ADD final_bill TO bills

        DISPLAY monthly billing details

    END FOR

    FOR each month from 2 to number_of_months

        previous_units = consumption[month - 2]
        current_units = consumption[month - 1]

        IF previous_units = 0 THEN

            IF current_units > 0 THEN
                DISPLAY "Unusual increase"

            ELSE
                DISPLAY "0% increase"
            END IF

        ELSE
            percentage_increase =
                ((current_units - previous_units) /
                previous_units) * 100

            IF percentage_increase > threshold THEN
                DISPLAY "Unusual increase"

            ELSE
                DISPLAY "Normal increase"
            END IF

        END IF

    END FOR

    FIND highest consumption in consumption list
    FIND highest bill in bills list

    DISPLAY monthly comparison report
    DISPLAY highest consumption
    DISPLAY highest electricity bill

STOP
```
