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

    def summary(self):
        """
        QuickSelect is an efficient algorithm for finding the kth smallest or kth largest 
        element in an unsorted array. It is similar to QuickSort but only recurses on 
        one side of the partitioned array, reducing unnecessary work.

        Approach:
        1. Select a pivot (commonly the last element).
        2. Partition the array such that:
        - Elements smaller than the pivot go to the left.
        - Elements larger than the pivot go to the right.
        - The pivot is placed at its correct sorted position.
        3. Check the pivot index:
        - If it matches k, return the value.
        - If k is smaller, recurse on the left half.
        - If k is larger, recurse on the right half.

        Time Complexity:
        - Average case: O(n) (Each partition reduces the search space)
        - Worst case: O(n²) (Occurs when the worst pivot is always chosen)
        
        Space Complexity:
        - O(1) for iterative implementations.
        - O(log n) recursion depth (best case), O(n) in the worst case.

        Key Insight:
        - QuickSelect is preferred for kth order statistics (kth smallest/largest)
        since it avoids full sorting (O(n log n)) and achieves O(n) expected time.
        """

        pass

sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))  # Expected: [1, 2, 3, 5] 
print(sol.sortArray([5, 1, 1, 2, 0, 0]))  # Expected: [0, 0, 1, 1, 2, 5]
print(sol.sortArray([-2, 3, -5]))  # Expected: [-5, -2, 3]
        