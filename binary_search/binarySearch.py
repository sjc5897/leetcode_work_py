def search(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums,target))

