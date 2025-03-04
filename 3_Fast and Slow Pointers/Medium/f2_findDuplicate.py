# NAIVE APPROACH 1 - O(n log n) SC O(1) #
# To sort array and iterate through arr
# If curr iter == next iter, then return True

# NAIVE APPROACH 2 - O(n) SC O(n) #
# Iterate through arr
# track none duplicate vals in a set == SC O(n)
# if val is in set, return the val. 
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         """ 
#         return repeated # if solution contains duplicate - there is only one duplicate
#         """

#         # TC == O(n) SC == O(n)
#         inSet = set()

#         for i in range(len(nums)):
#             if nums[i] in inSet:
#                 return nums[i]
#             else:
#                 inSet.add(nums[i])

        
        
from typing import List
import unittest
# Optimal Approach:
# TC == O(n) . SC == O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 
        return repeated # if solution contains duplicate - there is only one duplicate
        """

        # TC == O(n) SC == O(1)

        # fast and slow pointer initialization
        fastPointer, slowPointer = 0, 0

        # First detect cycle
        while True:
            fastPointer, slowPointer = nums[nums[fastPointer]], nums[slowPointer] # Move fast and slow pointer by 2 and 1 step respectively
            if fastPointer == slowPointer:
                break
        
        # The Find the entry point to return that point
        slowPointer = 0
        while slowPointer != fastPointer:
            slowPointer = nums[slowPointer]
            fastPointer = nums[fastPointer]

        
        return slowPointer

    def solutionApproach(self):
        """
        This problem requires detecting a duplicate number in an array of size `n + 1`, 
        where numbers range from `1` to `n`. The **Floyd’s Cycle Detection Algorithm** 
        (also known as Tortoise and Hare) is the optimal solution, achieving **O(n) time 
        complexity and O(1) space complexity** without auxiliary data structures.

        🚀 **Steps to Solve the Problem Efficiently:**
        
        1️⃣ **Establish Two Pointers (Fast and Slow)**
        - Initialize `slowPointer` and `fastPointer` to `nums[0]`.
        - These pointers simulate a linked list traversal, treating each value as 
            an index pointing to the next number.

        2️⃣ **Detect the Cycle in the Array**
        - Move:
            - `slowPointer` one step at a time (`slowPointer = nums[slowPointer]`).
            - `fastPointer` two steps at a time (`fastPointer = nums[nums[fastPointer]]`).
        - If a duplicate exists (which is guaranteed), **slow and fast will meet** inside the cycle.

        3️⃣ **Find the Cycle Entry Point (Duplicate Number)**
        - Reset `slowPointer` to `nums[0]`.
        - Move **both pointers one step at a time** until they meet again.
        - The meeting point is the **entry point of the cycle**, which is the duplicate number.

        4️⃣ **Return the Duplicate Number**
        - Either `slowPointer` or `fastPointer` now holds the duplicate.

        🔹 **Key Learnings:**
        - **This problem is a cycle detection problem disguised as an array problem.**
        - **The presence of a duplicate ensures a cycle exists.**
        - **The cycle entry point corresponds to the duplicate number.**
        
        ⏳ **Time Complexity:** O(n)  
        🏗 **Space Complexity:** O(1)
        """

class TestFindDuplicate(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        nums = [1, 2, 4, 2, 2]

        expectedOutput = 2

        self.assertEqual(self.sol.findDuplicate(nums), expectedOutput)

    def test_1(self):
        nums = [3, 1, 3, 4, 2]

        expectedOutput = 3

        self.assertEqual(self.sol.findDuplicate(nums), expectedOutput)

if __name__ == "__main__":
    unittest.main()
# sol = Solution()
# print(sol.findDuplicate([1,3,4,2,2])) # Expected: 2
# print(sol.findDuplicate([3,1,3,4,2])) # Expected: 3
# print(sol.findDuplicate([3,3,3,3,3])) # Expected: 3

        
        