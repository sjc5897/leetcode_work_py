#https://leetcode.com/problems/squares-of-a-sorted-array/


# represents the naive approach for this problem
def sortedSquares1(nums):
    for i in range(0,len(nums)):
        nums[i] = nums[i] ** 2
    return sorted(nums)

# two pointer approach
def sortedSquares2(nums):
    num_size = len(nums)
    left = 0
    right = num_size - 1

    result = [0 for i in range(num_size)]

    i = right
    while(i >= 0):
        if(abs(nums[left]) > nums[right]):
            result[i] = nums[left] ** 2
            left+=1
        else:
            result[i] = nums[right] ** 2
            right-=1
        i-=1

    return result



def sortedSquares(nums):
    return sortedSquares2(nums)