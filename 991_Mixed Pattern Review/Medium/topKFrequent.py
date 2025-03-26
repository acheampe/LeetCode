from collections import Counter
import heapq
import unittest

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        return k most frequent elements
        
        TC: O(n log k)
        SP: O(n)
        """
        
        # heapq.heapify(nums) # O(n)
        countFreq = Counter(nums)
        topKFrequent = []
        minHeap = []
          
        for num, freq in countFreq.items():
            heapq.heappush(minHeap, (freq, num))
            
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        while minHeap:
            freq, num = heapq.heappop(minHeap)
            topKFrequent.append(num)
                
        return  topKFrequent
                
                
            

        
            
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

    def test4_large_k(self):
        nums = [4,4,4,6,6,7,8,8,8,8]
        k = 3
        expectedOutput = [4, 8, 6]  # Most frequent elements in any order
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    def test5_duplicates_but_different_frequencies(self):
        nums = [10,10,10,20,20,30,30,30,30]
        k = 2
        expectedOutput = [30, 10]
        self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

    # def test6_mixed_positive_negative(self):
    #     nums = [-1, -1, -1, 2, 2, 3, 3, 3, 3]
    #     k = 2
    #     expectedOutput = [3, -1]
    #     self.assertCountEqual(self.sol.topKFrequent(nums, k), expectedOutput)

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