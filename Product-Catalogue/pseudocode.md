BEGIN

    SET number_of_products = 3
    CREATE empty list products

    FOR i FROM 1 TO 3

        INPUT product_id
        INPUT price
        INPUT stock_quantity

        CREATE tuple (product_id, price, stock_quantity)
        ADD tuple TO products

    END FOR

    SET total_inventory_value = 0
    SET invalid_records = 0
    SET replenishment_count = 0

    FOR each product IN products

        EXTRACT product_id, price, stock_quantity

        IF price <= 0 OR stock_quantity < 0 THEN

            DISPLAY "Invalid Product Record"
            INCREMENT invalid_records

        ELSE

            CALCULATE inventory_value = price * stock_quantity
            ADD inventory_value TO total_inventory_value

            IF stock_quantity <= 5 THEN

                DISPLAY "Replenishment Required"
                INCREMENT replenishment_count

            ELSE

                DISPLAY "Stock Sufficient"

            END IF

        END IF

    END FOR

    DISPLAY total_inventory_value
    DISPLAY invalid_records
    DISPLAY replenishment_count

END
