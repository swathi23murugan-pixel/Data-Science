a=float(input("Subject 1: "))
b=float(input("Subject 2: "))
c=float(input("Subject 3: "))

avg=(a+b+c)/3

print(f"Average: {avg:.2f}%")

if avg>=90:
    print("Grade A+")
elif avg>=75:
    print("Grade A")
elif avg>=50:
    print("Grade B")
else:
    print("Fail")