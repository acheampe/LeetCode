from typing import List

# Alternate approach:
# Is to determine n/2
# Then establish a dictionary to track count of each element
# And compare to n/2 after each update
# if value of dictonary of the key/element => n/2, then return that key
# This implementation will be O(n) for time and space complexity 


class Solution: # TC O(n log n) and SC O(log n) due to stack from recursive call
    # For the sake of practicing divide and conquer approach
    def majorityElement(self, nums: List[int]) -> int:
        """
        return the majority element that appears more than [n/2], n is size of nums
        """

        # Establish base case for termination: len of 0 is a majority
        if len(nums) <= 1:
            return nums[0]
        
        # Division phase:Split Into Two Halves
        mid = len(nums) // 2
        leftMaj = self.majorityElement(nums[:mid])
        rightMaj = self.majorityElement(nums[mid:])

        # Conquer Phase: Decide majority element phase
        if leftMaj == rightMaj: # if agreeable
            return leftMaj # or rightMaj, both will be the same values
        
        # If not agreeable, count returned val in each array
        leftCount = self.countOccurence(nums, leftMaj)
        rightCount = self.countOccurence(nums, rightMaj)

        return rightMaj if rightCount > leftCount else leftMaj
        
    
    def countOccurence(self, array, target):
        """
        return how many times target appears in array
        """

        count = 0

        for i in range(len(array)):
            if array[i] == target:
                count += 1
        
        return count

sol = Solution()
# print(sol.majorityElement([3,2,3])) # 3
print(sol.majorityElement([2,2,1,1,1,2,2])) # 2   