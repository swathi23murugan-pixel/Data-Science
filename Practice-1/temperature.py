c=float(input("Celsius: "))
f=(c*9/5)+32
k=c+273.15
print(f"Celsius: {c:.2f}°C")
print(f"Fahrenheit: {f:.2f}°F")
print(f"Kelvin: {k:.2f} K")
print("Conversion Table")
print("Celsius Fahrenheit Kelvin")
for i in range(-40,101,10):
    f=(i*9/5)+32
    k=i+273.15
    print(f"{i:.2f} {f:.2f} {k:.2f}")