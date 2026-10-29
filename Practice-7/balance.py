def find_max_length(nums):
    balance = 0
    positions = {0: -1}
    longest = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            balance = balance + 1
        else:
            balance = balance - 1
        if balance in positions:
            length = i - positions[balance]
            if length > longest:
                longest = length
        else:
            positions[balance] = i
    return longest

nums = [0, 1, 0]
print("Maximum balanced subarray length:", find_max_length(nums))