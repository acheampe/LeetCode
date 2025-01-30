from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        return the index of target value, if not in cycle arr, return -1

        Args: nums - list of CYCLE array; target --> [int] input that we 
        should look for in nums

        returns: int --> index containing our target value

        Time Complexity: O (log n)
        Space Complexity: O(log n) if considering stack
        """
        
        def findStartIndex(currLeft, currRight):
            """
            returns: int --> our startIndex
            """
            arrLen = len(nums)

            if currLeft >= currRight:
                return currLeft # startIndex that we are looking for (cases where startIndex is at either ends of nums)
            
            midpoint = currLeft + ((currRight - currLeft) // 2)

            # condition for midpoint index being our startIndex
            if nums[(midpoint % arrLen)] < nums[((midpoint - 1) % arrLen)]:
                return (midpoint % len(nums))
        

            return findStartIndex(midpoint + 1, (midpoint + 1) + currRight)
        
        self.startIndex = findStartIndex(0, len(nums) - 1)

        def binarySearchforIndex(startIndex, endIndex):
            """
            Modified binary search to find index
            """

            # base case:
            if startIndex >= endIndex:
                return startIndex % len(nums) # last selected is our target index
            
            midpoint = startIndex + ((endIndex - startIndex) // 2)

            if nums[(midpoint % len(nums))] == target:
                return midpoint % len(nums) # we found our target index
            
            elif nums[(midpoint % len(nums))] < target:
                return binarySearchforIndex(midpoint + 1, endIndex)
            
            else:
                return binarySearchforIndex(startIndex, midpoint - 1)

        indexResult = binarySearchforIndex(self.startIndex, self.startIndex + len(nums) - 1)
        
        return indexResult if nums[indexResult] == target else -1

        

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        expectedOutput = 4
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test2(self):
        nums = [1]
        target = 0
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test3(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    # Additional Test Cases

    def test4(self):
        nums = [6,7,0,1,2,4,5]
        target = 6
        expectedOutput = 0
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test5(self):
        nums = [6,7,0,1,2,4,5]
        target = 5
        expectedOutput = 6
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test6(self):
        nums = [3,4,5,6,7,8,9,10,1,2]
        target = 1
        expectedOutput = 8
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test7(self):
        nums = [3,4,5,6,7,8,9,10,1,2]
        target = 10
        expectedOutput = 7
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test8(self):
        nums = [30,40,50,10,20]
        target = 10
        expectedOutput = 3
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test9(self):
        nums = [1,2,3,4,5,6,7,8,9]
        target = 5
        expectedOutput = 4
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test10(self):
        nums = [1,2,3,4,5,6,7,8,9]
        target = 10
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test11(self):
        nums = [7,8,9,1,2,3,4,5,6]
        target = 3
        expectedOutput = 5
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test12(self):
        nums = [7,8,9,1,2,3,4,5,6]
        target = 9
        expectedOutput = 2
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test13(self):
        nums = [2,3,4,5,6,7,8,9,1]
        target = 1
        expectedOutput = 8
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test14(self):
        nums = [5,6,7,8,9,1,2,3,4]
        target = 8
        expectedOutput = 3
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test15(self):
        nums = [5,6,7,8,9,1,2,3,4]
        target = 6
        expectedOutput = 1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

if __name__ == '__main__':
    unittest.main()