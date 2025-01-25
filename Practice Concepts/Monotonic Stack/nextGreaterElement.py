from typing import List
# from collections import deque
import unittest

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        return the next greater element in input array nums
        """

        # memory needed for operation
        stack = [(nums[0], 0)]
        result = [-1] * len(nums)
    

        # establish iteration:
        for i in range(1, len(nums)):

            stackElement, index = stack[-1]
            # maintain decreasing monotonic stack
            while stack and stackElement < nums[i]: # no longer decreasing if added

                result[index] = nums[i] # we have found our next greater element
                stack.pop() # remove element to maintain monotonic decreasing stack
            
            stack.append((nums[i], i))
        
        return result
                



class testNextGreaterElement(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test1(self):

        nums = [1,2,1]

        expectedOutput = [2,-1,2]

        self.assertEqual(self.sol.nextGreaterElements(nums), expectedOutput)
    
    # def test2(self):
        
    #     nums = [1,2,3,4,3]

    #     expectedOutput = [2,3,4,-1,4]

    #     self.assertTrue(self.sol.nextGreaterElements(nums), expectedOutput)

if __name__ == '__main__':
    unittest.main()