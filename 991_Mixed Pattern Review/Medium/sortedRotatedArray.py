import unittest

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        return index of target if target in nums
        
        TC: O(log n)
        SC: O(1)
        
        QUICK Summary: Main trick is to figure out which side is ordered, then 
        based of that decide which side to search for our target value. 
        """
        
        leftIndex, rightIndex = 0, len(nums) - 1
        
        while leftIndex < rightIndex:
            
            midIndex = leftIndex + (rightIndex - leftIndex) // 2
            
            if nums[midIndex] == target:
                return midIndex
            
            elif nums[leftIndex] <= nums[midIndex]: # means left side is the ordered side
                
                if (nums[leftIndex] <= target < nums[midIndex]):
                    rightIndex = midIndex - 1
                
                else:
                    leftIndex = midIndex + 1
            
            else:
                if (nums[rightIndex] >= target > nums[midIndex]):
                    leftIndex = midIndex + 1
                
                else:
                    rightIndex = midIndex - 1
        
        return leftIndex if nums[leftIndex] == target else -1
    
class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.search([4,5,6,7,0,1,2], 0), 4)

    def test_example_2(self):
        self.assertEqual(self.sol.search([4,5,6,7,0,1,2], 3), -1)

    def test_example_3(self):
        self.assertEqual(self.sol.search([1], 0), -1)

    def test_not_rotated(self):
        self.assertEqual(self.sol.search([1, 2, 3, 4, 5], 3), 2)

    def test_rotated_at_middle(self):
        self.assertEqual(self.sol.search([6,7,8,1,2,3,4,5], 2), 4)

    def test_single_element_found(self):
        self.assertEqual(self.sol.search([10], 10), 0)

    def test_large_array_target_absent(self):
        nums = list(range(1000, 10000)) + list(range(1, 999))
        self.assertEqual(self.sol.search(nums, -1), -1)

    def test_large_array_target_present(self):
        nums = list(range(1000, 10000)) + list(range(1, 999))
        self.assertEqual(self.sol.search(nums, 1234), nums.index(1234))

    def test_example_0(self):
        self.assertEqual(self.sol.search([1,3], 3), 1)

if __name__ == "__main__":
    unittest.main()