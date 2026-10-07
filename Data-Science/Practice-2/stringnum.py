text=input()
text=text.lstrip()
sign=1
i=0
if i<len(text) and text[i] in "+-":
    if text[i]=="-":
        sign=-1
    i+=1
num=0
found=False
while i<len(text) and text[i].isdigit():
    num=num*10+int(text[i])
    i+=1
    found=True
if found:
    print(sign*num)
else:
    print(0)