a=int(input("Number 1: "))
b=int(input("Number 2: "))
def convert(n,base):
    chars="0123456789ABCDEF"
    result=""
    while n>0:
        result=chars[n%base]+result
        n//=base
    return result or "0"
x=a
while x>0:
    x//=1
print("Binary :",convert(a,2))
print("Octal :",convert(a,8))
print("Hexadecimal :",convert(a,16))
x,y=a,b
while y:
    x,y=y,x%y
gcd=x
print("GCD :",gcd)
print("LCM :",a*b//gcd)