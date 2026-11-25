print("REPEATED TRANSACTION DETECTION")

number_of_transactions = int(input("Enter number of transactions: "))

if number_of_transactions <= 0:

    print("Invalid number of transactions")

else:

    transaction_ids = []

    for i in range(1, number_of_transactions + 1):

        transaction_id = input("Enter transaction ID: ").upper()

        transaction_ids.append(transaction_id)

    repeated_transactions = []

    for transaction_id in transaction_ids:

        count = transaction_ids.count(transaction_id)

        if count > 1 and transaction_id not in repeated_transactions:

            repeated_transactions.append(transaction_id)

    print("\n---------- TRANSACTION SUMMARY ----------")

    print("Total Transactions:", number_of_transactions)

    if len(repeated_transactions) > 0:

        print("\nRepeated Transactions:")

        for transaction_id in repeated_transactions:

            print(transaction_id, "-", transaction_ids.count(transaction_id), "times")

        print("Number of Repeated Transaction IDs:", len(repeated_transactions))

    else:

        print("No repeated transactions found")

    print("-----------------------------------------")