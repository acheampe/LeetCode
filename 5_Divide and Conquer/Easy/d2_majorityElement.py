from typing import List

# Alternate approach:
# Is to determine n/2
# Then establish a dictionary to track count of each element
# And compare to n/2 after each update
# if value of dictonary of the key/element => n/2, then return that key
# This implementation will be O(n) for time and space complexity 


class Solution: # TC O(n) SC O(1)
    def majorityElement(self, nums: List[int]) -> int:
        """
        return the majority element that appears more than [n/2], n is size of nums
        """

        # Since majority is gauranteed in each input we will use Bayer Moore Voting Algo Approach

        count, currMaj = 0, 0 

        for i in range(len(nums)):

            if count == 0:
                currMaj = nums[i]
                count += 1
            
            elif count > 0 and currMaj == nums[i]:
                count += 1

            else:
                count -= 1
            
        return currMaj

sol = Solution()
# print(sol.majorityElement([3,2,3])) # 3
# print(sol.majorityElement([2,2,1,1,1,2,2])) # 2   
print(sol.majorityElement([6, 5, 5])) # 5