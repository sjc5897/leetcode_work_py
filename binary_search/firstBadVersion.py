# https://leetcode.com/problems/first-bad-version/
def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 1, n

    while left < right:

        mid = left + (right - left) // 2

        # again this problem uses a blackbox method
        # if isBadVersion(mid):
        #     right = mid
        # else:
        #     left = mid + 1

    return left