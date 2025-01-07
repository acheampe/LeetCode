from typing import List

class Solution: # Best/Average TC = O(n log n), worse case O(n^2), if partition point is the largest or smallest in the group array, and SC = O(log n), worse case O(n)
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort array using quicksort (in-place)."""
        
        # Step 1: initiate quick sorting recursion
        
        self.quickSort(nums, 0, len(nums) - 1)

        return nums

    def quickSort(self, nums, low, high):
        """Recursive call to sort arr with partitioning"""

        # Step 2: quick sort subarrays

        if low >= high:
            return 
        
        # use pivot point to divide array not inclusive of pivot for sorting
        pivotIndex = self.partition(nums, low, high)
        self.quickSort(nums, pivotIndex + 1, high)
        self.quickSort(nums, low, pivotIndex - 1)

    def partition(self, nums, low, high):
        """partition to return ordered index"""

        # Step 3: partition to find appropriate location of pivot value
        pivot = high
        i = low - 1

        for j in range(low, high):
            
            if nums[j] < nums[pivot]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        # position pivot in it's right location
        nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1]

        return i + 1 # for correct location of pivot


       

sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))  # Expected: [1, 2, 3, 5] 
print(sol.sortArray([5, 1, 1, 2, 0, 0]))  # Expected: [0, 0, 1, 1, 2, 5]
print(sol.sortArray([-2, 3, -5]))  # Expected: [-5, -2, 3]
        