# Assumptions

1. The user enters the total number of transactions.
2. The number of transactions must be greater than zero.
3. Each transaction has a unique ID under normal circumstances.
4. A transaction ID appearing more than once is considered a repeated transaction.
5. Transaction IDs are treated as case-insensitive. For example, TX101 and tx101 are considered the same ID.
6. The program assumes that the user enters valid transaction IDs.
7. The program identifies repeated IDs only once in the final summary, along with their occurrence counts.
