def quick(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        quick(nums, left, partition_pos - 1)
        quick(nums, partition_pos + 1, right)


def partition(nums, left, right):
    i = left
    j = right


nums = [3, 7, 20, 47, 77, 82, 18, 72, 54, 96]