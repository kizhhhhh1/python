def count_smaller(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

# Example usage
nums = [8, 1, 2, 2, 3]
print(count_smaller(nums))  # Output: [4, 0, 1, 1, 2]
