store_a = {'LED': 20, 'Cable': 10, 'Board': 3}
store_b = {'Cable': 5, 'Sensor': 7, 'LED': 8}
result = store_a.copy()
for item in store_b:
    if item in result:
        result[item] += store_b[item]
    else:
        result[item] = store_b[item]
print("Combined inventory:", result)