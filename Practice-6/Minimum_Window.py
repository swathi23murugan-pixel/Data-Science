s = 'ADOBECODEBANC'
t = 'ABC'
need = {}
for char in t:
    need[char] = need.get(char, 0) + 1
left = 0
count = 0
start = 0
minimum = len(s) + 1
window = {}
for right in range(len(s)):
    char = s[right]
    window[char] = window.get(char, 0) + 1
    if char in need and window[char] <= need[char]:
        count += 1
    while count == len(t):
        if right - left + 1 < minimum:
            minimum = right - left + 1
            start = left
        first = s[left]
        window[first] -= 1
        if first in need and window[first] < need[first]:
            count -= 1
        left += 1
if minimum == len(s) + 1:
    print("Minimum window: ''")
else:
    print("Minimum window:", repr(s[start:start + minimum]))