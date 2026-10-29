def top_k_frequent(nums, k):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] = frequency[num] + 1
        else:
            frequency[num] = 1
    result = []
    for i in range(k):
        max_num = None
        for num in frequency:
            if max_num is None or frequency[num] > frequency[max_num]:
                max_num = num
        if max_num is not None:
            result.append(max_num)
            del frequency[max_num]
    return result

nums = [1, 1, 1, 2, 2, 3]
print("Top 2 frequent values:", top_k_frequent(nums, 2))