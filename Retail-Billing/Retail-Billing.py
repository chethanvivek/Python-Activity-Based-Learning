print("RETAIL BILLING WITH MULTIPLE DISCOUNT RULES")

number_of_items = int(input("Enter number of items: "))

if number_of_items <= 0:
    print("Invalid number of items")

else:
    subtotal = 0
    valid = True

    for i in range(1, number_of_items + 1):

        print("\nItem", i)

        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid item details")
            valid = False
            break

        item_total = price * quantity
        subtotal = subtotal + item_total

    if valid:

        if subtotal < 500:
            purchase_discount = subtotal * 0.05

        elif subtotal < 2500:
            purchase_discount = subtotal * 0.10

        else:
            purchase_discount = subtotal * 0.15

        amount_after_discount = subtotal - purchase_discount

        membership = input("\nIs the customer a member? (yes/no): ").lower()

        if membership == "yes":
            membership_discount = amount_after_discount * 0.05

        elif membership == "no":
            membership_discount = 0

        else:
            membership_discount = -1

        if membership_discount == -1:
            print("Invalid membership status")

        else:
            final_amount = amount_after_discount - membership_discount

            print("\n---------- RETAIL BILL ----------")
            print("Subtotal             : ₹", format(subtotal, ".2f"))
            print("Purchase Discount    : ₹", format(purchase_discount, ".2f"))
            print("Membership Discount  : ₹", format(membership_discount, ".2f"))
            print("---------------------------------")
            print("Final Payable Amount : ₹", format(final_amount, ".2f"))
            print("---------------------------------")