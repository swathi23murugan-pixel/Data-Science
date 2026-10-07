year=int(input("Year: "))
marks=float(input("Marks: "))
if year%400==0 or (year%4==0 and year%100!=0):
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")
if marks<0 or marks>100:
    print("Invalid marks. Enter a value between 0 and 100.")
elif marks>=90:
    print("Grade: A+")
elif marks>=75:
    print("Grade: A")
elif marks>=50:
    print("Grade: B")
else:
    print("Grade: Fail")