from typing import List
import random

class Solution: # Aeverage Case Complexity: O(n), Worse Case: O(n^2) if pivot
    # is the smallest or largest val; Space complexity = O (log n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Return the Kth largest element
        """

        # Step One: Call Quick Select to only sort concerned portion
        self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

        return nums[len(nums) - k]
    
    def quickSelect(self, nums, low, high, desiredIndex):
        """
        Seeks to find desired Index where Kth element is located
        """
        while low <= high:
            # Step 1: Choose pivot using median-of-three
            pivotIndex = self.medianOfThree(nums, low, high)
            nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]  # Move pivot to the end

            # Step 2: Partition around the pivot
            pivotIndex = self.partition(nums, low, high)

            # Step 3: Narrow the search
            if pivotIndex == desiredIndex:
                return  # Found the desired index
            elif pivotIndex < desiredIndex:
                low = pivotIndex + 1
            else:
                high = pivotIndex - 1
    
    def partition(self, nums, low, high):
        """
        Find the right index position for pivot
        """

        # Step 3: Find appropriate position for pivot val and return that index
        i = low - 1
        pivot = high

        for j in range(low, high):

            if nums[j] < nums[pivot]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]

        # Position pivot value at appropriate index
        nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1]

        return i + 1 # appropriate index of pivot

    def medianOfThree(self, nums, low, high):
        """
        Select the pivot as the median of the first, middle, and last elements.
        """
        mid = (low + high) // 2
        a, b, c = nums[low], nums[mid], nums[high]

        # Find the median value
        if (a <= b <= c) or (c <= b <= a):
            return mid
        elif (b <= a <= c) or (c <= a <= b):
            return low
        else:
            return high


sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2)) # Expected: 5
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # Expected: 4
# Passes 41/42 test cases

