from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        return indices of values that adds up to target
        """

        # Questions:
        # can input arr be empty?
        # Can input array be manipulated?
        # will all input vals be integers?, will there be any negative vals i should consider?
        # will target input always be an int, any chance of a negative target?
        # Can't use the same elements twice, does this mean that their indices have to be different
        # or does that not matter?
        # will length of input arr always be atleast 2?
        

        ### first approach ###
        isComplementSum = defaultdict(int)

        for i, val in enumerate(nums):
        
            if val in isComplementSum:
                return [isComplementSum[val], i]
            isComplementSum[target - val] = i
        
        return -1 # we should never reach this point based on constraints (always one valid answer)


# class Solution: # ONLY IF SORTING THE INPUT ARRAY OR A COPY OF IT IS ALLOWED
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_copy = [(val, i) for i, val in enumerate(nums)]
#         nums_copy.sort()  # Sort by value, not index

#         left, right = 0, len(nums) - 1
#         while left < right:
#             curr_sum = nums_copy[left][0] + nums_copy[right][0]
#             if curr_sum == target:
#                 return [nums_copy[left][1], nums_copy[right][1]]
#             elif curr_sum < target:
#                 left += 1
#             else:
#                 right -= 1

#         return -1
sol = Solution()

sol.twoSum([3,2,4], 6)

