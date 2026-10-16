n = int(input())
a = list(map(int, input().split()))
p = neg = z = even = odd = both = only3 = only5 = neither = 0
for i in a:
    if i > 0:
        p += 1
    elif i < 0:
        neg += 1
    else:
        z += 1
    if i != 0:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if i % 3 == 0 and i % 5 == 0:
        both += 1
    elif i % 3 == 0:
        only3 += 1
    elif i % 5 == 0:
        only5 += 1
    else:
        neither += 1
print("Positive:", p)
print("Negative:", neg)
print("Zero:", z)
print("Even:", even)
print("Odd:", odd)
print("Divisible by both 3 and 5:", both)
print("Divisible only by 3:", only3)
print("Divisible only by 5:", only5)
print("Divisible by neither:", neither)