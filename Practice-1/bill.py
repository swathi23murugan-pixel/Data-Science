items=[]
while True:
    x=input("Enter price: ")
    if x.lower()=="done":
        break
    items.append(float(x))
subtotal=sum(items)
if subtotal>=500:
    discount=subtotal*0.10
else:
    discount=subtotal*0.05
tax=(subtotal-discount)*0.05
total=subtotal-discount+tax
print("Item Price")
print("-----------------")
for i,x in enumerate(items,1):
    print(f"Item {i} {x:.2f}")
print("-----------------")
print(f"Subtotal {subtotal:.2f}")
print(f"Discount {discount:.2f}")
print(f"Tax {tax:.2f}")
print(f"Final {total:.2f}")