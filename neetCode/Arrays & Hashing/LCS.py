import unittest
import heapq

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         """return the longest consecutive in array"""
        
#         if not nums:
#             return 0 
        
#         minHeap = list(set(nums[:])) # O(n), incase input can't be manipulated
#         maxCounter = 1 # for current Val
        
#         heapq.heapify(minHeap)
#         currVal = heapq.heappop(minHeap)
#         currCount = 1
        
#         while minHeap:
            
#             currPop = heapq.heappop(minHeap) # TC O(log k) for each pop but will sum to O(n)
#             while currVal + 1 == currPop:
#                 currCount += 1
#                 currVal = currPop
#                 if minHeap:
#                     currPop = heapq.heappop(minHeap)
            
#             else:
#                 maxCounter = max(maxCounter, currCount)
#                 currCount = 1
#                 currVal = currPop
            
#         return maxCounter
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # only start counting if it's the start of a sequence
            if num - 1 not in numSet:
                current = num
                streak = 1

                while current + 1 in numSet:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
    
class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [2, 20, 4, 10, 3, 4, 5]
        expected = 4  # [2, 3, 4, 5]
        self.assertEqual(self.sol.longestConsecutive(nums), expected)

    def test_example_2(self):
        nums = [0, 3, 2, 5, 4, 6, 1, 1]
        expected = 7  # [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(self.sol.longestConsecutive(nums), expected)

    def test_single_element(self):
        nums = [100]
        expected = 1
        self.assertEqual(self.sol.longestConsecutive(nums), expected)

    def test_empty_array(self):
        nums = []
        expected = 0
        self.assertEqual(self.sol.longestConsecutive(nums), expected)

    def test_all_duplicates(self):
        nums = [1, 1, 1, 1]
        expected = 1
        self.assertEqual(self.sol.longestConsecutive(nums), expected)

    def test_disjoint_sequences(self):
        nums = [10, 5, 6, 3, 4, 20, 21]
        expected = 3  # [3, 4, 5, 6] is not possible since 5 and 6 are split; longest = [20, 21] or [3, 4, 5]
        self.assertEqual(self.sol.longestConsecutive(nums), 4)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, 0, 1, 2]
        expected = 6  # [-3, -2, -1, 0, 1, 2]
        self.assertEqual(self.sol.longestConsecutive(nums), expected)

if __name__ == '__main__':
    unittest.main()