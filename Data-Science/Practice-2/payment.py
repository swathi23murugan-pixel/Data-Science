n=int(input("Transactions: "))
values=[]
rejected=0
for i in range(n):
    x=input()
    try:
        x=float(x)
        if x<0:
            rejected+=1
        else:
            values.append(x)
    except:
        rejected+=1
print("Successful Transactions :",len(values))
print(f"Total Amount : ₹{sum(values):.2f}")
if values:
    print(f"Highest Transaction : ₹{max(values):.2f}")
    print(f"Lowest Transaction : ₹{min(values):.2f}")
    print(f"Average Transaction : ₹{sum(values)/len(values):.2f}")
print("Rejected Transactions :",rejected)