x=input("Enter value: ")
print("Original value type : str")
try:
    a=int(x)
    print("Integer value :",a)
    print("Integer type : int")
except:
    print("Invalid integer conversion")
try:
    b=float(x)
    print("Float value :",b)
    print("Float type : float")
except:
    print("Invalid float conversion")