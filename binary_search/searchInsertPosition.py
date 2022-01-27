# https://leetcode.com/problems/search-insert-position/submissions/
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return right + 1


if __name__ == "__main__":
    nums = [1,2,5,6]
    target = 5
    print(searchInsert(nums,target))
