text = input("Enter a message: ")
shift = int(input("Enter shift value: "))
choice = input("Encode or decode (e/d): ").lower()

if choice == "d":
    shift = -shift

result = ""

for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch

print("Result:", result)