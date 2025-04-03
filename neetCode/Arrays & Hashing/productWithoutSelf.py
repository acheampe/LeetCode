import unittest

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """return product except self in the array"""
        
        # Questions:
        # any empty arrays?
        # do i whave do worry about floats? or unsuspecting types but int?
        # Can input arrays be directly manipulated?
        
        def discussApproachWithInterview():
            """One approach i can take is iterating through the array and finding the 
            product of the current index except self. This approach is bruteforce and
            will take approx. quadratic complexity...I think we can be faster
            
            The other approach we can take is duplicating nums to twice it's current len to
            stimulate a cyclic array  and find the product of the next k-1 indices as it's sum
            product for linear complexity with O(n) space complexity - (CORRECTION
             - this is still quadratic complexity), this will be the
            approach i use unless I recall the prefix sum strategy in the next few minutes.
            """

        result = [1] * len(nums)

        #calc. prefix values
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
            
        #calc. suffix
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]
        
        return result
                

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(self.sol.productExceptSelf(nums), expected)

    # def test_example_2(self):
    #     nums = [-1, 1, 0, -3, 3]
    #     expected = [0, 0, 9, 0, 0]
    #     self.assertEqual(self.sol.productExceptSelf(nums), expected)

    # def test_all_ones(self):
    #     nums = [1, 1, 1, 1]
    #     expected = [1, 1, 1, 1]
    #     self.assertEqual(self.sol.productExceptSelf(nums), expected)

    # def test_with_negative_numbers(self):
    #     nums = [2, -2, 3, 4]
    #     expected = [-24, 24, -16, -12]
    #     self.assertEqual(self.sol.productExceptSelf(nums), expected)

    # def test_with_two_elements(self):
    #     nums = [3, 5]
    #     expected = [5, 3]
    #     self.assertEqual(self.sol.productExceptSelf(nums), expected)

    # def test_with_multiple_zeros(self):
    #     nums = [0, 0, 1, 2]
    #     expected = [0, 0, 0, 0]
    #     self.assertEqual(self.sol.productExceptSelf(nums), expected)

    # def test_with_single_zero(self):
    #     nums = [0, 1, 2, 3]
    #     expected = [6, 0, 0, 0]
    #     self.assertEqual(self.sol.productExceptSelf(nums), expected)

if __name__ == '__main__':
    unittest.main()