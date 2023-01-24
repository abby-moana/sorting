def merge(nums):
    if len(nums) > 1:
        left_nums = nums[:len(nums)//2]
        right_nums = nums[len(nums)//2:]

        merge(left_nums)
        merge(right_nums)




nums = [3, 7, 20, 47, 77, 82, 18, 72, 54, 96]
merge(nums)

print(nums)
