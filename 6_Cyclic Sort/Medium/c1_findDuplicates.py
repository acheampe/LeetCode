from typing import List

class Solution: # TC == O(n) and SC == O(n)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        return all integers that appears at most twice
        """
        #EXPLORE SIGN MARKING AND OTHER CYCLIC SORT SOLUTION TO MEET REQ.
    
        # Edge case where nums.length = 1:
        if len(nums) == 1:
            return [] # no duplicate can be found here

        # Initiate variables: lenght, result arr
        duplicatesFound = set()

        # Use cyclic sort and tag duplicates
        for i in range(len(nums)):

            if nums[i] != i + 1:   # If no match 
                while nums[i] != nums[nums[i] - 1]: # swap till there is a match
                    nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] - 1]
                
                if nums[i] == nums[nums[i] - 1] and nums[i] != i + 1:
                    duplicatesFound.add(nums[i])

        return list(duplicatesFound)
        

sol = Solution()
print(sol.findDuplicates([1,1,2]))  # Expected: [1]
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Expected: [2, 3]
print(sol.findDuplicates([5,4,6,7,9,3,10,9,5,6]))  # Expected: [9,5,6]
print(sol.findDuplicates([2,1]))  # Expected: []        
