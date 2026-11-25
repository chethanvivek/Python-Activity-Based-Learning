### 6. `pseudocode.md`

```text
BEGIN

    INPUT number_of_transactions

    IF number_of_transactions <= 0 THEN
        DISPLAY "Invalid number of transactions"

    ELSE

        CREATE empty list transaction_ids

        FOR i FROM 1 TO number_of_transactions

            INPUT transaction_id
            CONVERT transaction_id TO uppercase
            ADD transaction_id TO transaction_ids

        END FOR

        CREATE empty list repeated_transactions

        FOR each transaction_id IN transaction_ids

            SET count = number of occurrences of transaction_id

            IF count > 1 AND transaction_id NOT IN repeated_transactions THEN

                ADD transaction_id TO repeated_transactions

            END IF

        END FOR

        DISPLAY total number of transactions

        IF repeated_transactions is not empty THEN

            DISPLAY "Repeated Transactions"

            FOR each transaction_id IN repeated_transactions

                DISPLAY transaction_id
                DISPLAY its occurrence count

            END FOR

            DISPLAY number of repeated transaction IDs

        ELSE

            DISPLAY "No repeated transactions found"

        END IF

    END IF

END
```
