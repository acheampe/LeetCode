from typing import List
from collections import defaultdict
import unittest


## Alternative, smoother approach:
## sort the input array first before entering backtracking loop
## back track through inclusive branch (or exclusive)
## pop to backtrack
## the use while logic to skip duplicates (since you ordered input)
## then backtrack through exclusive route

# Time complexity: O(n * 2^n)
# Space Complexity: Worse case O(n) if each element is unique for dictionary; O(h) for stack if tree is balanced

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Return subsets without duplicates.
        """
        def findNonDupSubsets(arrSet, subSet, index):
            # Base case: end of array
            if index == len(arrSet):
                result.append(subSet[:])  # Append the current subset
                return
            
            # Include current element
            subSet.append(arrSet[index])
            findNonDupSubsets(arrSet, subSet, index + 1)
            
            # Exclude current element (backtrack)
            subSet.pop()
            
            # Skip duplicates
            while index + 1 < len(arrSet) and arrSet[index] == arrSet[index + 1]:
                index += 1
            
            findNonDupSubsets(arrSet, subSet, index + 1)
        
        result = []
        nums.sort()  # Sort input to ensure subsets are generated in lexicographical order
        findNonDupSubsets(nums, [], 0)
        return result
    
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         """
#         return subsets without duplicates
#         """

#         def findNonDupSubsets(arrSet, subSet, index):
#             """
#             return unique subsets
#             Time complexity: O(n * 2^n)
#             Space Complexity: Worse case O(n) if each element is unique for dictionary; O(h) for stack if tree is balanced
#             """

#             # Condition to return from current subset:
#             if index == len(arrSet):

#                 sortSubset = sorted(subSet) # n log n operation

#                 # Only add to result if unique
#                 if not trackSet[tuple(sortSubset)]:
#                     result.append(sortSubset)
#                     trackSet[tuple(sortSubset)] = True
#                 return
            
#             # Non inclusive element
#             findNonDupSubsets(arrSet, subSet, index + 1)

#             # Inclusive element
#             subSet.append(arrSet[index])
#             findNonDupSubsets(arrSet, subSet, index + 1)

#             # Backtrack
#             subSet.pop()
        
#         result = [] # append unique subsets here
#         trackSet = defaultdict(bool) # to track if subset is unique or not (worse case: O(n) space), but O(1) lookup
#         findNonDupSubsets(nums, [], 0)

#         return result
        
        

class testSubsetsWithDup(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test1(self):
        nums = [1, 2, 2]
        expectedOutput = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        self.assertCountEqual(self.sol.subsetsWithDup(nums), expectedOutput)

    def test2(self):
        nums = [0]
        expectedOutput = [[], [0]]
        self.assertCountEqual(self.sol.subsetsWithDup(nums), expectedOutput)
    
    def test3(self):
        nums = [1, 2, 2, 3]
        expectedOutput = [
            [], [1], [2], [3], [1, 2], [1, 3], [2, 2], [2, 3], 
            [1, 2, 2], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]
        ]
        self.assertCountEqual(self.sol.subsetsWithDup(nums), expectedOutput)
    
    def test4(self):
        nums = [4, 4, 4, 1, 4]
        expectedOutput = [
            [], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4],
            [1, 4, 4, 4], [4, 4, 4, 4], [1, 4, 4, 4, 4]
        ]
        self.assertCountEqual(self.sol.subsetsWithDup(nums), expectedOutput)
    
    def test5(self):
        nums = []
        expectedOutput = [[]]
        self.assertCountEqual(self.sol.subsetsWithDup(nums), expectedOutput)

if __name__ == '__main__':
    unittest.main()