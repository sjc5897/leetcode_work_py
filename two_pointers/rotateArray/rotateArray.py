
# https://leetcode.com/problems/rotate-array/
# https://www.youtube.com/watch?v=BHr381Guz3Y

# first base, used extra array
def rotate1(nums,k):
    n = len(nums)
    k = k % n

    sol = [0]*n

    i = 0
    while(i < n):
        sol[(i + k) % n] = nums[i]
    nums = sol



def rotate(nums, k):
    rotate1(nums,k)