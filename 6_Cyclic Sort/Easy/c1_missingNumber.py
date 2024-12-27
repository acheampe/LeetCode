from typing import List

class Solution: # TC = O(n). SC = O(1)
    def missingNumber(self, nums: List[int]) -> int:
        """
        return the only number in the range that is missinfg from the array
        """
        # Questions to determine approach:
        # Is range always defined from 0 - n, appears so and it is inclusive []
        # Can problem be addressed without additional DS? In-place algorithm

        # Sorting Phase:
        for i in range(len(nums)):

            # Skip if out of bound
            if nums[i] >= len(nums):
                continue
            
            # Swap out of order values
            while nums[i] != i and nums[i] < len(nums):
                # Swap places
                missVal = nums[i]
                missVal2 = nums[nums[i]]
                nums[nums[i]] = missVal
                nums[i] = missVal2

        
        # Iterate through sorted arr for missing number
        for i in range(len(nums)):
            if i != nums[i]:
                return i # Early termination because we found missing number
            
        return len(nums) # As the missing number 

sol = Solution()
print(sol.missingNumber([3,0,1])) # Expected: 2
print(sol.missingNumber([0,1])) # Expected: 2
print(sol.missingNumber([9,6,4,2,3,5,7,0,1])) # Expected: 8