from typing import List

class Solution:  # Time Complexity: O(n log n), Space Complexity: O(n)
    def sortArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Practice quick sort - returns element greater than pivot
        to it's right and less than pivot to its left
        """

        i = - 1

        for j in range(len(nums) - 1): # exclusing pivot position
            
            # Do nothing if j val is greater than pivot val for partitioning
            if nums[j] > nums[pivot]:
                continue # j increments

            else: # increment i and swap with j val to partition
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                # j increments automatically
            
        # Swap pivot val with i + 1 val
        nums[pivot], nums[i + 1] = nums[i + 1], nums[pivot]
            
        return nums

sol = Solution()
# print(sol.sortArray([5, 2, 3, 1], len([5, 2, 3, 1]) - 1)) # Expected: [1, 2, 3, 5]
# print(sol.sortArray([5, 1, 1, 2, 0, 0], len([5, 1, 1, 2, 0, 0]) - 1))  # Expected: [0, 0, 1, 2, 5, 1]
# print(sol.sortArray([-2, 3, -5], len([-2, 3, -5]) - 1))  # Expected: [-5, 3, -2]