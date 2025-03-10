transactions_aed = [3500.75, 2500.50, 400.25, 800.99, 1800.45, 2500.30, 600.10, 900.95, 300.60, 500.20, 700.75, 450.40, 3000.99, 2200.85, 150.55]

transactions_usd = []

i = 0

while i <=len(transactions_aed)-1:
    item_usd = transactions_aed[i] * 0.27
    print("converting value", transactions_aed[i])
    transactions_usd.append(item_usd)
    i += 1

for item in transactions_aed:
    item_usd = item * 0.27
    print("converting value", item)
    transactions_usd.append(item_usd)


print(transactions_usd)