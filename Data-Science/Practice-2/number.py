start=int(input("Start: "))
end=int(input("End: "))
print("Number Prime Perfect Armstrong Palindrome Digit Sum Digits Binary")
for n in range(start,end+1):
    if n<2:
        prime="No"
    else:
        prime="Yes"
        for i in range(2,n):
            if n%i==0:
                prime="No"
                break
    total=0
    temp=n
    while temp>0:
        total+=temp%10
        temp//=10
    perfect=sum(i for i in range(1,n) if n%i==0)==n if n>0 else False
    digits=len(str(n))
    arm=sum(int(x)**digits for x in str(n))==n
    palindrome=str(n)==str(n)[::-1]
    print(n,prime,"Yes" if perfect else "No","Yes" if arm else "No","Yes" if palindrome else "No",total,digits,bin(n)[2:])