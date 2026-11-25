BEGIN

    INPUT number_of_items

    IF number_of_items <= 0 THEN
        DISPLAY "Invalid number of items"

    ELSE

        subtotal = 0
        valid = TRUE

        FOR each item from 1 to number_of_items

            INPUT price
            INPUT quantity

            IF price < 0 OR quantity <= 0 THEN
                DISPLAY "Invalid item details"
                valid = FALSE
                BREAK
            END IF

            item_total = price * quantity
            subtotal = subtotal + item_total

        END FOR

        IF valid = TRUE THEN

            IF subtotal < 500 THEN
                purchase_discount = subtotal * 0.05

            ELSE IF subtotal < 2500 THEN
                purchase_discount = subtotal * 0.10

            ELSE
                purchase_discount = subtotal * 0.15
            END IF

            amount_after_discount = subtotal - purchase_discount

            INPUT membership_status

            IF membership_status = "yes" THEN
                membership_discount = amount_after_discount * 0.05
            ELSE
                membership_discount = 0
            END IF

            final_amount = amount_after_discount - membership_discount

            DISPLAY subtotal
            DISPLAY purchase_discount
            DISPLAY membership_discount
            DISPLAY final_amount

        END IF

    END IF

END
