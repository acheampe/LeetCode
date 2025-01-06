from typing import List

class Solution: # Best/Average TC = O(n log n), worse case O(n^2), if partition point is the largest or smallest in the group array, and SC = O(log n), worse case O(n)
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort array using quicksort (in-place)."""
        
        self.quicksort(nums, 0, len(nums) - 1)

        return nums

    def quicksort(self, arr, low, high):
        """quicksort using partitioning"""

        if low < high:
            pivotIndex = self.partition(arr, low, high)
            self.quicksort(arr, low, pivotIndex - 1)
            self.quicksort(arr, pivotIndex + 1, high) # avoid slicing since that creates a new array


    def partition(self, arr, low, high):
        """partition to return index"""

        # step 1: track pivot placement ( i + 1 index)
        i = low - 1
        pivot = high
        
        # step 2: iter for pivot point placement
        for j in range(low, high):

            if arr[j] <= arr[pivot]:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        
        # step 3: Place pivot value in it's true position
        arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]

        # Step 4: return pivot index
        return i + 1

sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))  # Expected: [1, 2, 3, 5] 
# print(sol.sortArray([5, 1, 1, 2, 0, 0]))  # Expected: [0, 0, 1, 1, 2, 5]
# print(sol.sortArray([-2, 3, -5]))  # Expected: [-5, -2, 3]
        