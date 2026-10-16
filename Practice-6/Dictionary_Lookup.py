stock = {'LED': 20, 'RESISTOR': 50, 'SENSOR': 4}
requested = ['LED', 'SENSOR', 'SWITCH']
for item in requested:
    if item in stock:
        print(item + ':', stock[item], 'available')
    else:
        print(item + ': unavailable')