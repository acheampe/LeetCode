from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Return all elements that appears at most twice

        Args: Arr - List of Integers

        Return: List of integers that appeared at most twice

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        duplicateResult = []
        # Edge case:
        if len(nums) == 1:
            return [] # no duplicate with lenght of 1
        
        # seek duplicate indices, to determine duplicate
        for i in range(len(nums)):

            associatedIndex = abs(nums[i]) - 1

            if nums[associatedIndex] < 0:

                # means that we there is a duplicate pointer value
                duplicateResult.append(abs(nums[i]))
            
            else: # mark as an explored option

                nums[associatedIndex] = -nums[associatedIndex]
        
        return duplicateResult

# # Different approach if input preservation is required:
# def findDuplicates(nums: List[int]) -> List[int]:
#     seen = [False] * len(nums)  # O(n) space
#     duplicates = []

#     for num in nums:
#         index = abs(num) - 1  # Map to index
#         if seen[index]:
#             duplicates.append(abs(num))  # Found duplicate
#         else:
#             seen[index] = True  # Mark as seen

#     return duplicates

sol = Solution()
# print(sol.findDuplicates([1,1,2]))  # Expected: [1]
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Expected: [2, 3]
# print(sol.findDuplicates([5,4,6,7,9,3,10,9,5,6]))  # Expected: [9,5,6]
# print(sol.findDuplicates([2,1]))  # Expected: []      
