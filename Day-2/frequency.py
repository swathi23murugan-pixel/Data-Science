text="Python is easy and Python is powerful"
words=text.lower().split()
count={}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)