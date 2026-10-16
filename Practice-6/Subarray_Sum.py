nums = [1, 1, 1]
k = 2
count = 0
total = 0
prefix = {0: 1}
for num in nums:
    total += num
    count += prefix.get(total - k, 0)
    prefix[total] = prefix.get(total, 0) + 1
print("Count:", count)