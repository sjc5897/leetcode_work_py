import unittest

from two_pointers.rotateArray import rotateArray


class MyTestCase(unittest.TestCase):
    # constraints
    # 1 <= nums.length <= 10 ^ 5
    # -2 ^ 31 <= nums[i] <= 2 & 31 - 1
    # 0 <= k <= 10 ^ 5

    def test_example_1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        rotateArray.rotate(nums,k)
        sol = [5,6,7,1,2,3,4]
        self.assertEqual(sol,nums)

    def test_example_2(self):
        nums = [-1,-100,3,99]
        k = 2
        rotateArray.rotate(nums, k)
        sol = [3,99,-1,-100]
        rotateArray.rotate(nums,k)
        self.assertEqual(sol, nums)

    def test_example_len_1(self):
        nums = [1]
        k = 3
        rotateArray.rotate(nums, k)
        sol = [1]
        rotateArray.rotate(nums, k)
        self.assertEqual(sol, nums)

    def test_example_k_0(self):
        nums = [1,2,3,4,5,6,7,8,9,10]
        k = 0
        rotateArray.rotate(nums, k)
        sol = [1,2,3,4,5,6,7,8,9,10]
        rotateArray.rotate(nums, k)
        self.assertEqual(sol, nums)

    def test_example_k_greater_than_n(self):
        nums = [1,2,3,4,5]
        k = 6
        rotateArray.rotate(nums, k)
        sol = [5,1,2,3,4]
        rotateArray.rotate(nums, k)
        self.assertEqual(sol, nums)

if __name__ == '__main__':
    unittest.main()
