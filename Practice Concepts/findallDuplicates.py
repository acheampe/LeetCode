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
    
    def approachSolution(self):
        """
        The best way to address this problem while meeting constraint is to use sign marker. 

        There are a couple way to go about using sign marker but to realize this, you must communicate
        with your interviewer. 
            - Establish if you are allowed to manipute the input values.
            - if not, then copy the whole input value, but establish that this will take O(n) space.
        
        If iinterviewer expects auxillary space of O(1) then estalish that the only way
        to do this is to manipulate values in input array with sign

        So essentially, to find all duplicated in range 1 - n. Treat values within the
        input array as index pointers (nums[nums - 1]), and if the value in that 
        index is > 0, change sign to negative (we are taking advantage of positive contraint values).
        Then iterate to the next, if we come to the next iteration and it's pointer leads to a negative
        value, then we know we have found one duplicate, which is then added to result array.

        If input array cannot be manipulated and have established that space of O(n) is fine to use, 
        then either copy input array to a new array and use establish solution above, or you can 
        make an array == length input array with bolean false values of length of array [False] * len(inputArray)

        Then iterate through input array, and use it's respective value pointer to see if boleanArray has been checked,
        if not check (false), turn to True, if True, then we add our input array value to resultArr to return. 
        """

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
