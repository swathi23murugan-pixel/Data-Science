password = input()
upper = lower = digit = special = False
for i in password:
    if i.isupper():
        upper = True
    elif i.islower():
        lower = True
    elif i.isdigit():
        digit = True
    else:
        special = True
if len(password) >= 8 and upper and lower and digit and special:
    print("Valid password")
else:
    print("Invalid password")
print("Uppercase:", "Present" if upper else "Missing")
print("Lowercase:", "Present" if lower else "Missing")
print("Digit:", "Present" if digit else "Missing")
print("Special character:", "Present" if special else "Missing")
print("Minimum length:", "Satisfied" if len(password) >= 8 else "Not satisfied")