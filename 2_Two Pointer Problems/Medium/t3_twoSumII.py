from typing import List
import unittest
# TC == O(n) SC == O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        return indexes in order of its values that sums to target
        """

        startIndex, endIndex = 0, len(numbers) - 1

        while startIndex < endIndex:
            
            currTotalVal = numbers[startIndex] + numbers[endIndex] 
            if currTotalVal == target:
                return [startIndex + 1, endIndex + 1]
            
            elif currTotalVal > target:
                endIndex -= 1
            
            else:
                startIndex += 1
        
        return []

class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        nums = [2,7,11,15]
        target = 9

        expectedOutput = [1, 2]

        self.assertEqual(self.sol.twoSum(nums, target), expectedOutput)
    
if __name__ == "__main__":
    unittest.main()

        