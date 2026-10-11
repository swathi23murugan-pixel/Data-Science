text=input("Message: ")
shift=int(input("Shift: "))
encrypted=""
for x in text:
    if x.isupper():
        encrypted+=chr((ord(x)-65+shift)%26+65)
    elif x.islower():
        encrypted+=chr((ord(x)-97+shift)%26+97)
    else:
        encrypted+=x
decrypted=""
for x in encrypted:
    if x.isupper():
        decrypted+=chr((ord(x)-65-shift)%26+65)
    elif x.islower():
        decrypted+=chr((ord(x)-97-shift)%26+97)
    else:
        decrypted+=x
print("Encrypted:",encrypted)
print("Decrypted:",decrypted)