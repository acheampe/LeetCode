from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Performs modified binary search on a sorted list to find nonduplicate num

        Args:
            nums (List[int]): Sorted list of integers, with only one 
            nonduplicate, all others are duplicate pairs. 

        Returns:
            int: The index of the target in nums, or -1 if not found.

        Time Complexity: O(log n)
        Space Complexity: O(1), O(log n) if considering recursive stack
        """

        def modifiedBinarySearch(start, end):
            """
            returns nonduplicate

            Args: Start and end[int] boundaries to stay within valid boundaries

            returns: int of nonduplicate value
            """

            # Base/return case:
            if start >= end:
                return nums[start] # this is our nonduplicate
            
            midIndex = start + ((end - start) // 2)

            if nums[midIndex] != nums[midIndex - 1] and nums[midIndex] != nums[midIndex + 1]:
                return nums[midIndex]
            
            # conditions to check left side
            elif midIndex % 2 == 0 and nums[midIndex] != nums[midIndex + 1] or \
                midIndex % 2 == 1 and nums[midIndex] == nums[midIndex + 1]:
                return modifiedBinarySearch(start, midIndex - 1)
            
            else: # otherwise checks right
                return modifiedBinarySearch(midIndex + 1, end)   

        return modifiedBinarySearch(0, len(nums) - 1)
    
    def approachStrategy(self):
        """
        Summary Approach: 

        To solve this is log n, we will need a modified binary search.

        To approach this, we will need to define boundaries of our array at
        every iteration.

        After that, we define our midpoint;
        then compare midpoint values to it's left val and right val to see 
        if there is an equal value to either side.

        if there isn't, then we have found our unique value, if there is then we
        determine which side we need to search to find the nonduplicate value
        by looking to see if index pattern is off

        if index of middle is even and it has an equivalent value to its right adjacent
        index, then the pattern still holds and we can check the right side, otherwise we check the 
        left side. 
        """

        pass
    
            
sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # Expected Output: 2
print(sol.singleNonDuplicate([3,3,7,7,10,11,11])) # Expected Output: 10