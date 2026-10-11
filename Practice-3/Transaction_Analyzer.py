n = int(input("Enter number of transactions: "))
transactions = []

for i in range(n):
    amount = float(input("Enter transaction amount: "))
    if amount >= 0:
        transactions.append(amount)
    else:
        print("Invalid transaction")

if len(transactions) > 0:
    print("Total:", sum(transactions))
    print("Maximum:", max(transactions))
    print("Minimum:", min(transactions))
    print("Average:", sum(transactions) / len(transactions))
else:
    print("No valid transactions")