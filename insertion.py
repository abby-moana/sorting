def insertion(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1

            print(nums)


nums = [3, 7, 20, 47, 77, 82, 18, 72, 54, 96]
insertion(nums)

print(nums)
