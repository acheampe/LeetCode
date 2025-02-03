from typing import List
from collections import Counter
import heapq
import unittest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        returns a list of k frequent numbers in list 

        Args: List of array (nums), k[int] for topK frequent

        return: List[int]

        Time Complexity O(n log k)
        Space Complexity O(k) 
        """

        # first initiate counter of array and min_Heap
        countDic = Counter(nums) # O(n) operation
        min_heap = []
        kFrequent = [] # return variable

        # heappush min frequency, num as a tuple group
        for num, freq in countDic.items(): # O(n) 
            
            heapq.heappush(min_heap, (freq, num)) # O (log k) operation
        
             # To reduce min_heap to the top k frequent vals
            if len(min_heap) > k:
                heapq.heappop(min_heap) # O(log k) operation each
        
        while min_heap:
            # unwrap tuple and append val
            freq, val = heapq.heappop(min_heap)

            kFrequent.append(val) # O(k) space
        
        return kFrequent
    
    def approachStrategy(self):
        """
        To solve this problem efficiently, we first need a dictionary, to track 
        frequency of each value, this is performed in O(n), you can use
        Counter from collections to perform this to maintain code simplicity

        Following this we want to iterate through the freq, val of the dictionary
        and push to a new array as heappush by converting freq, val to a tuple (freq, val)

        As we heappush we track min_heap to make sure len is never > k, if it is,
        we heappop. By the end of this cycle we should have all top K frequent.

        From here iterate through min_heap to append val to result array.

        **Time Complexity:** O(n log k)
            - O(n) to count frequencies
            - O(n log k) to push into the heap and maintain size k
            - O(k log k) for extracting results (optional sorting step, but not necessary)
    
        **Space Complexity:** O(k)
            - O(k) for the heap storing the top k elements
        """


class TestTopKFrequent(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test1_basic_case(self):
        nums = [1,1,1,2,2,3]
        k = 2
        expectedOutput = [1,2]  # Order does not matter
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    def test2_single_element(self):
        nums = [1]
        k = 1
        expectedOutput = [1]
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    # def test3_all_unique_elements(self):
    #     nums = [5, 9, 3, 7, 1]
    #     k = 3
    #     expectedOutput = [5, 9, 3]  # Any 3 elements in the array are valid
    #     self.assertCountEqual(len(self.sol.topKFrequent(nums, k)), expectedOutput)

    # def test4_large_k(self):
    #     nums = [4,4,4,6,6,7,8,8,8,8]
    #     k = 3
    #     expectedOutput = [4, 8, 6]  # Most frequent elements in any order
    #     self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    def test5_duplicates_but_different_frequencies(self):
        nums = [10,10,10,20,20,30,30,30,30]
        k = 2
        expectedOutput = [30, 10]
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    def test6_mixed_positive_negative(self):
        nums = [-1, -1, -1, 2, 2, 3, 3, 3, 3]
        k = 2
        expectedOutput = [3, -1]
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    def test7_large_input(self):
        nums = [i % 10 for i in range(100000)]  # Generates numbers 0-9 repeated evenly
        k = 5
        output = self.sol.topKFrequent(nums, k)
        self.assertEqual(len(output), k)

    def test8_large_numbers(self):
        nums = [10000, 10000, 10000, -9999, -9999, 5000, 5000, 5000, 5000]
        k = 2
        expectedOutput = [5000, 10000]
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    def test9_k_equals_unique_elements(self):
        nums = [7, 7, 8, 8, 9, 9, 10, 10]
        k = 4
        expectedOutput = [7, 8, 9, 10]  # All elements are equally frequent
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    def test10_single_frequency_high_k(self):
        nums = [42] * 1000
        k = 1
        expectedOutput = [42]
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

if __name__ == '__main__':
    unittest.main()