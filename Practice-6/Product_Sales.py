sales = {'Sensor': [4, 6, 5], 'Cable': [10, 2, 3], 'Board': [8, 7], 'LED': [5, 5, 5]}
result = {}
for product in sales:
    result[product] = sum(sales[product])
for product in sorted(result, key=lambda x: (-result[x], x)):
    print(product + ':', result[product])