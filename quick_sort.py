def quick(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        quick(nums, left, partition_pos - 1)
        quick(nums, partition_pos + 1, right)


def partition(nums, left, right):
    i = left
    j = right
    pivot = nums[right]

    while i < j:
        while i < right and nums[i] < pivot:
            i += 1

        while j > left and nums[j] >= pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    if nums[i] > pivot:
        nums[i], nums[right] = nums[right], nums[i]

    return i


nums = [3, 7, 20, 47, 77, 82, 18, 72, 54, 96]
quick(nums, 0, len(nums) - 1)
