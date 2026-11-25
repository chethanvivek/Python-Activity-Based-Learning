print("TUPLE-BASED PRODUCT CATALOGUE AUDIT")

number_of_products = 3
products = []

for i in range(1, number_of_products + 1):

    print("\nProduct", i)

    product_id = input("Enter product ID: ")
    price = float(input("Enter product price: "))
    stock_quantity = int(input("Enter stock quantity: "))

    product = (product_id, price, stock_quantity)

    products.append(product)


total_inventory_value = 0
invalid_records = 0
replenishment_count = 0

print("\n---------- PRODUCT CATALOGUE AUDIT ----------")

for product in products:

    product_id = product[0]
    price = product[1]
    stock_quantity = product[2]

    print("\nProduct ID:", product_id)

    if price <= 0 or stock_quantity < 0:

        print("Invalid Product Record")
        invalid_records = invalid_records + 1

    else:

        inventory_value = price * stock_quantity
        total_inventory_value = total_inventory_value + inventory_value

        print("Inventory Value: ₹", format(inventory_value, ".2f"))

        if stock_quantity <= 5:

            print("Status: Replenishment Required")
            replenishment_count = replenishment_count + 1

        else:

            print("Status: Stock Sufficient")


print("\n---------- AUDIT SUMMARY ----------")

print("Total Products:", number_of_products)
print("Invalid Records:", invalid_records)
print("Products Requiring Replenishment:", replenishment_count)
print("Total Inventory Value: ₹", format(total_inventory_value, ".2f"))

print("-----------------------------------")