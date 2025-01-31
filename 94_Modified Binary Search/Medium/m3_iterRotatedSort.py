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
        Space Complexity: O(l1) 
        """
        
        startIndex, endIndex = 0, len(nums) - 1 # inclusive boundaries

        while startIndex <= endIndex:

            # calculate current mid
            mid = startIndex + ((endIndex - startIndex) // 2)

            # return condition
            if nums[mid] == target:
                return mid # we have the desired index
            
            # check to find which side is an ordered array and use to decide which half to search
            elif nums[startIndex] <= nums[mid]: # means left side is ordered
                if target >= nums[startIndex] and target < nums[mid]:
                    endIndex = mid - 1 # search left side
                
                else:
                    startIndex = mid + 1
            
            elif nums[endIndex] > nums[mid]: # means right side is ordered
                if target <= nums[endIndex] and target > nums[mid]:
                    startIndex = mid + 1  # search right side

                else:
                    endIndex = mid - 1 # check left side
            


        # if target is not found, check last val at startIndex
        return -1 

### Point of struggle here was not considering add constraint to find the ordered
### side first to see if target is in that side, if it is search that side, if not
### search the other side. Make sure that one of the check conditions for left side
### has an equal evaluator (in this case >=) to evaluate when arrays comes down to two to iterate approriately
 

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