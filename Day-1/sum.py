n=int(input("N: "))

i=1
total=0

while i<=n:
    total+=i
    i+=1

average=total/n

print("Sum:",total)
print(f"Average: {average:.2f}")