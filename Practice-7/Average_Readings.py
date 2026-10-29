def average_readings(*args):
    if len(args) == 0:
        return None

    total = 0
    for num in args:
        total = total + num

    return total / len(args)

print("Average:", average_readings(10, 20, 30, 40))

result = average_readings()
if result is None:
    print("No readings provided")