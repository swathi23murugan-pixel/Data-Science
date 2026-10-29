def longest_consecutive(nums):
    numbers = set(nums)
    longest = 0
    for num in numbers:
        count = 1
        current = num
        while current + 1 in numbers:
            current = current + 1
            count = count + 1
        if count > longest:
            longest = count
    return longest

nums = [100, 4, 200, 1, 3, 2]
print("Longest consecutive sequence length:", longest_consecutive(nums))