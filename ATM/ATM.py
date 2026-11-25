print("ATM TRANSACTION SEQUENCE SIMULATION")

initial_balance = float(input("Enter initial account balance: "))
number_of_transactions = int(input("Enter number of transactions: "))

if initial_balance < 0 or number_of_transactions <= 0:

    print("Invalid initial details")

else:

    balance = initial_balance
    total_deposits = 0
    total_withdrawals = 0
    successful_transactions = 0
    rejected_transactions = 0

    for i in range(1, number_of_transactions + 1):

        print("\nTransaction", i)

        transaction_type = input(
            "Enter transaction type (deposit/withdrawal): "
        ).lower()

        amount = float(input("Enter transaction amount: "))

        if amount <= 0:

            print("Transaction rejected: Invalid amount")
            rejected_transactions = rejected_transactions + 1

        elif transaction_type == "deposit":

            balance = balance + amount
            total_deposits = total_deposits + amount
            successful_transactions = successful_transactions + 1

            print("Deposit successful")

        elif transaction_type == "withdrawal":

            if amount > 10000:

                print("Transaction rejected: Withdrawal limit exceeded")
                rejected_transactions = rejected_transactions + 1

            elif amount > balance:

                print("Transaction rejected: Insufficient balance")
                rejected_transactions = rejected_transactions + 1

            else:

                balance = balance - amount
                total_withdrawals = total_withdrawals + amount
                successful_transactions = successful_transactions + 1

                print("Withdrawal successful")

        else:

            print("Transaction rejected: Invalid transaction type")
            rejected_transactions = rejected_transactions + 1

    print("\n---------- ATM TRANSACTION SUMMARY ----------")
    print("Initial Balance          : ₹", format(initial_balance, ".2f"))
    print("Total Deposits           : ₹", format(total_deposits, ".2f"))
    print("Total Withdrawals        : ₹", format(total_withdrawals, ".2f"))
    print("Successful Transactions  :", successful_transactions)
    print("Rejected Transactions    :", rejected_transactions)
    print("Final Account Balance    : ₹", format(balance, ".2f"))
    print("---------------------------------------------")