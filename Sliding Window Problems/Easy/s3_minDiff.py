from typing import List

# Time complexity O(nlogn) and Space complexity O(1)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        Return the minimum difference in k window of students
        """
        numsLen = len(nums)

        # Edge case: k > numsLen (unlikely due to constraints)
        if k > numsLen:
            return -1 
        
        # If only one student is picked, difference is always 0
        if numsLen == 1:
            return 0
        
        # Sort the array to ensure minimal differences between consecutive values
        nums.sort()
        
        # Initialize the sliding window pointers
        startIndex = 0
        endIndex = k - 1
        
        min_diff = float('inf')  # Set initial minimum difference to infinity
        
        # Slide the window across the array
        while endIndex < numsLen:
            min_diff = min(min_diff, nums[endIndex] - nums[startIndex])
            startIndex += 1
            endIndex += 1

        return min_diff

#### ATTEMPT O(n) solution  - Frequency count ####

# Test Cases
sol = Solution()
print(sol.minimumDifference([9, 4, 1, 7], 2))  # Expected: 2
print(sol.minimumDifference([9], 1))  # Expected: 0
print(sol.minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6))  # Expected: 74560
