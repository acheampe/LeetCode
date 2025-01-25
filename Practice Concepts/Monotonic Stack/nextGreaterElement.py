from typing import List
# from collections import deque
import unittest

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        return the next greater element in input array nums
        """

        # Establishing memory needed for operation
        stack = []
        resultArr = [-1] * len(nums)

        for i in range(len(nums) * 2): # for passing 2x through array (stimulates a circular arr)

            circularIndex = i % len(nums)

            # Logic loop to maintain monotonic stack
            while stack and nums[stack[-1]] < nums[circularIndex]:

                # found our next greater value
                resultArr[stack.pop()] = nums[circularIndex]

            
            if i < len(nums):
                stack.append(i)
        
        return resultArr



class testNextGreaterElement(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test1(self):

        nums = [1,2,1]

        expectedOutput = [2,-1,2]

        self.assertEqual(self.sol.nextGreaterElements(nums), expectedOutput)
    
    def test2(self):
        
        nums = [1,2,3,4,3]

        expectedOutput = [2,3,4,-1,4]

        self.assertTrue(self.sol.nextGreaterElements(nums), expectedOutput)

    def test3(self):
        
        nums = [1,2,3,4,5]

        expectedOutput = [2,3,4,5,-1]

        self.assertTrue(self.sol.nextGreaterElements(nums), expectedOutput)

if __name__ == '__main__':
    unittest.main()


# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         """
#         return the next greater element in input array nums
#         """

#         # S1: Establish memory for operation:
#         stack = [] 
#         resultArr = [-1] * len(nums) # returns outcome
#         CountAppends = len(resultArr) - 1

#         # S2: iterate through input arr
#         for i in range(len(nums)):

#             circularIndex = i

#             if stack:
#                 stackElement, stackIndex = stack[-1]

#             while stack and stackElement <= nums[circularIndex]:
                
#                 # ignore equal elements and process to next index
#                 if stackElement == nums[circularIndex]:
#                     circularIndex = (circularIndex + 1) % len(nums)
#                     continue

#                 # append next greater element and count append
#                 resultArr[stackIndex] = nums[circularIndex]
#                 CountAppends -= 1

#                 # early return condition
#                 if CountAppends == 0:
#                     return resultArr # we've found all over next greater values
                
#                 # pop stack to maintain decreasing monotonic constraint
#                 stack.pop()
#                 # append and update stack[-1] variable
#                 stack.append((nums[circularIndex], circularIndex))
#                 stackElement, stackIndex = stack[-1]

#                 # increment circular index
#                 circularIndex = (circularIndex + 1) % len(nums)

#             else:
#                 stack.append((nums[circularIndex], circularIndex))

            
#         return resultArr