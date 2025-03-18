import unittest
from unittest import result

# class Solution:
#     def lengthOfLIS(self, nums: list[int]) -> int:
#         """
#         Compute the length of the longest increasing subsequence (LIS).
#         DP Approach: Bottom-Up
#         Time Complexity: O(n^2)
#         Space Complexity: O(n)
#         """

#         if not nums:
#             return 0
        
#         memo = [1] * len(nums)
        
#         for i in range(len(nums)):
#             for j in range(i):
                
#                 if nums[j] < nums[i]:
#                     memo[i] = max(memo[j] + 1, memo[i])
        
#         return max(memo)
    
#     def ApproachSolution(self):
#         """
#         This problem can be solved with a couple approaches, binary search and 
#         dynamic programming approach. 
        
#         Utilizing dynamic program:
#         step 1: validate input nums and establish an array of length input nums with default values of int
#         1.
        
#         step two: 
#         establish a nested loop. Outer loop will be of len(nums) and inner loops
#         will be of the current index.
        
#         Step three:
#         Evaluate if nums[j] (inner loop) < outer loop index (nums[i]). if so add current
#         value of index j of established array to current count of index i of established array
        
#         Step four: return the max val in the established array
        
#         TC: O(n^2) nested loop of the same input array
#         SC: O(n) established space to find max subsequent increasing array
#         """
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Longest Increasing Subsequence (O(n log n))
        Uses Greedy + Binary Search (without bisect module)
        """
        
        def binary_search(sub, num):
            """
            Custom binary search to find the first index in `sub`
            where `num` can be placed while keeping `sub` sorted.
            """
            left, right = 0, len(sub) - 1

            while left <= right:
                mid = (left + right) // 2
                
                if sub[mid] < num:
                    left = mid + 1  # Search right half
                else:
                    right = mid - 1  # Search left half
            
            return left  # The position where num should be placed

        sub = []  # Stores the potential LIS elements
        
        for num in nums:
            pos = binary_search(sub, num)  # Find position manually
            
            if pos < len(sub):
                sub[pos] = num  # Replace element at `pos`
            else:
                sub.append(num)  # Append num at the end if no replacement

        return len(sub)  # The length of `sub` is the LIS length
class TestSolution(unittest.TestCase):
    def test_lengthOfLIS(self):
        sol = Solution()
        
        # Basic test cases
        self.assertEqual(sol.lengthOfLIS([10,9,2,5,3,7,101,18]), 4)
        self.assertEqual(sol.lengthOfLIS([0,1,0,3,2,3]), 4)
        self.assertEqual(sol.lengthOfLIS([7,7,7,7,7,7,7]), 1)

        # Edge cases
        self.assertEqual(sol.lengthOfLIS([1]), 1)  # Single element
        self.assertEqual(sol.lengthOfLIS([10,20,30,40]), 4)  # Already increasing
        self.assertEqual(sol.lengthOfLIS([4,10,4,3,8,9]), 3)  # Random sequence
        
        # Large input case
        self.assertEqual(sol.lengthOfLIS(list(range(2500))), 2500)  # Strictly increasing

if __name__ == "__main__":
    unittest.main()