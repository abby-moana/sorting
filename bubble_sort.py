def sort(nums):
    for i in range(len(nums) -1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

                print(nums)


nums = [3, 7, 20, 47, 77, 82, 18, 72, 54, 96]
sort(nums)

print(nums)
