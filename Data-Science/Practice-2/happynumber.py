n=int(input())
seen=set()
while n!=1 and n not in seen:
    seen.add(n)
    total=0
    for x in str(n):
        total+=int(x)**2
    n=total
print(n==1)