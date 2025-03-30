import heapq
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        decide if input nums contains duplicate
        """
        
        # nums.sort()  # Overall TC O(n log n)
        # for i in range(len(nums) - 1): # O(n) TC
            
        #     if nums[i] == nums[i + 1]:
        #         return True
        
        # return False # No duplicate found; Overall SC O(1)
        # #################################

        # heapq.heapify(nums) # O(n)
        # temp = heapq.heappop(nums)

        # while nums:
            
        #     if nums[0] == temp:
        #         return True
            
        #     temp = heapq.heappop(nums)

        # return False # Overall SC O(1)
        # ##################################

        # nonDuplicate = defaultdict() # SC O(n)
        
        # for num in nums: # TC O(n)
        #     if num not in nonDuplicate:
        #         nonDuplicate[num] = True
        #     else:
        #         return nonDuplicate[num]
        
        # return False
        ####################################
        nonDuplicate = set() # SC O(n)
        
        for num in nums: # TC O(n)
            if num not in nonDuplicate:
                nonDuplicate.add(num)
            else:
                return True
        
        return False

        # This approach is cleaner becuase we do not modify input arr
        # Do not assume that modifying input array is ok, ask interviewer!
        # Clarify if all values will be an integer, if not, how to handle 
        # the exceptions
        # If constraints are provided look at those to determine if there are any
        # edge cases to worry about or to not worry about.