names = ['Anu', 'Arun', 'Bala', 'Banu', 'Cathy', 'Asha']
result = {}
for name in names:
    letter = name[0].upper()
    if letter not in result:
        result[letter] = []
    result[letter].append(name)
print(result)