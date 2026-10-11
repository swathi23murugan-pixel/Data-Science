text="aabbcdde"
for i in text:
    if text.count(i)==1:
        print(i)
        break
else:
    print(None)