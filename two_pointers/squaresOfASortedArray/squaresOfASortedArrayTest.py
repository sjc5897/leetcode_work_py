import unittest

from two_pointers.squaresOfASortedArray import squaresOfASortedArray


class MyTestCase(unittest.TestCase):
    def test_example_1(self):
        nums = [-4,-1,0,3,10]
        sol = [0,1,9,16,100]
        nums = squaresOfASortedArray.sortedSquares(nums)
        self.assertEqual(sol,nums)

    def test_example_2(self):
        nums = squaresOfASortedArray.sortedSquares([-7,-3,2,3,11])
        sol = [4,9,9,49,121]
        self.assertEqual(sol,nums)

    def test_size_0(self):
        nums = squaresOfASortedArray.sortedSquares([])
        sol = []
        self.assertEqual(sol,nums)

    def test_size_1(self):
        nums = squaresOfASortedArray.sortedSquares([2])
        sol = [4]
        self.assertEqual(sol, nums)



if __name__ == '__main__':
    unittest.main()
