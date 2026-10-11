n = int(input("Enter number of subjects: "))
total = 0

for i in range(n):
    mark = float(input("Enter mark: "))
    total += mark

average = total / n

print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")