from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lastNonZeroFoundAt = 0  # Pointer to place the next non-zero element

        # Step 1: Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1

        # Step 2: Fill the rest of the array with zeros
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         for i in range(len(nums)):
#             # i val  != 0 - increase nonZero Index

#             lastNonZeroVal = i

#             if nums[i] != 0:
#                 lastNonZeroVal += 1
            
#             else:
#                 while lastNonZeroVal < len(nums) and nums[lastNonZeroVal] == 0:
#                     lastNonZeroVal += 1
                
#                 else:
#                     if lastNonZeroVal < len(nums):
#                         nums[i], nums[lastNonZeroVal] = nums[lastNonZeroVal], nums[i]
        
#         return nums
       

sol = Solution() 
print(sol.moveZeroes([4,2,4,0,0,3,0,5,1,0])) # Expected: [4,2,4,3,5,1,0,0,0,0]
print(sol.moveZeroes([0,1,0,3,12])) # Expected: [1,3,12,0,0]    
print(sol.moveZeroes([0])) # Expected: [0]    

        