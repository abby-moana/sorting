def sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums

nums = [3, 7, 20, 47, 77, 82, 18, 72, 54, 96]
sort(nums)

print(nums)