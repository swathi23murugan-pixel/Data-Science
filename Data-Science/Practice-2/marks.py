n=int(input("Students: "))
print("Student Total Average Grade")
for i in range(n):
    name=input("Name: ")
    marks=input("Marks: ").split()
    try:
        marks=list(map(float,marks))
        if any(x<0 or x>100 for x in marks):
            print(name,"Invalid marks")
        else:
            total=sum(marks)
            avg=total/len(marks)
            if avg>=90:
                grade="A+"
            elif avg>=75:
                grade="A"
            elif avg>=50:
                grade="B"
            else:
                grade="Fail"
            print(name,int(total),f"{avg:.2f}",grade)
    except:
        print(name,"Invalid marks")