basic=float(input("Basic Salary: "))
hra=basic*0.20
da=basic*0.15
pf=basic*0.08
net=basic+hra+da-pf

print(f"HRA: {hra:.2f}")
print(f"DA: {da:.2f}")
print(f"PF: {pf:.2f}")
print(f"Net Salary: {net:.2f}")