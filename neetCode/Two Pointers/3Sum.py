# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         """return all tripets in an array that sums to 0"""
        
#         def discussQuestionApproach():
#             """
#             Given the constraints I do not have to worry about input arr len
#             less than 3 nor should I worry about at empty input
            
#             if none is found, I will return an empty array
            
#             I can use a 3 pointer system to find the answer in O(n^2) TC and
#             O(1) space complexity, not calculating for output array
#             """
#             pass
#         # Given that input arr can be sorted:
#         nums.sort()
#         result = [] # returns lists that sums to 0
        
#         for i in range(len(nums)):
            
#             # To avoid duplicates
#             if i != 0 and nums[i] == nums[i - 1]:
#                 continue #skips current iter in order to avoid duplicates
            
#             j, k = i + 1, len(nums) - 1
            
#             while j < k:
#                 total = nums[i] + nums[j] + nums[k]
#                 if total == 0:
#                     result.append([nums[i], nums[j], nums[k]])
                    
#                     # Move j and skip duplicates
#                     j += 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1

#                     # Move k and skip duplicates
#                     k -= 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1

#                 elif total < 0:
#                     j += 1
#                 else:
#                     k -= 1


                               
#         return result      
        
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """return all triplets in input nums that sums to 0"""

        result = []
        nums.sort()

        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i - 1]:
                continue # avoid duplicates
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # To avoid duplicate results
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                
                elif total > 0:
                    k -= 1
                
                else:
                    j += 1
            
        return result
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4])) # Expected: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1])) # Expected: []
print(sol.threeSum([0,0,0])) # Expected: [[0,0,0]]
print(sol.threeSum([3,-2,1,0])) # Expected: []
print(sol.threeSum([1,-1,0])) # Expected: [[-1,0,1]]
print(sol.threeSum([1,2,-2,-1])) # Expected: []
print(sol.threeSum([1,-1,-1,0])) # Expected: [[-1,0,1]]
print(sol.threeSum([-2,0,1,1,2])) # Expected: [[-2,0,2],[-2,1,1]]

