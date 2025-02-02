from typing import List
import unittest
import heapq

class Solution: 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Return the Kth largest element
        Time Complexity - O(n log k)
        Space complexity - O(k)
        """
        kLengthArray = [] # O (k) space operation

        for i in range(len(nums)):

            # adds current val to kLength heap array
            heapq.heappush(kLengthArray, nums[i])

            # keeps heap array at k length to maintain the k largest values
            if len(kLengthArray) > k:

                heapq.heappop(kLengthArray)
            
        # returns the kth's input
        return kLengthArray[0]
    
    def approachStrategy(self):
        """
        There are two ways to approach this using heap. The first and more
        efficient way when considering space complexity is utilizing a maxheap,
        however make sure to ask if values can be modified before using this 
        approach.

        To use maxheap, first, iterate through the array and convert values to
        its opposite value

        Second, heapify array, then pop off k-1, then return the kths value.
        This will return the kth largest in n log k TC and O(1) SC.

        If values cant be modified, establish new K length array.
        Iterate through array and heappush to K length array, if K length array 
        > than k, then heappop. 

        when array iteration is done, it will have the kth largest array, return 
        the first value of that kthlength araay and you will have your kth largest.
        The TC == O (n log k) and SC == O (k)
        """
        pass


class TestKthLargestFunc(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        expectedOutcome = 5
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)
    
    def test2(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        expectedOutcome = 4
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test3_single_element(self):
        nums = [10]
        k = 1
        expectedOutcome = 10
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test4_all_same_elements(self):
        nums = [7,7,7,7,7,7,7]
        k = 3
        expectedOutcome = 7
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test5_negative_numbers(self):
        nums = [-1,-2,-3,-4,-5]
        k = 2
        expectedOutcome = -2
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test6_mixed_positive_and_negative(self):
        nums = [-10, 4, 5, -3, 2, 8, -1]
        k = 3
        expectedOutcome = 4
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test7_large_k(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 10
        expectedOutcome = 1
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test8_k_equals_length(self):
        nums = [10, 20, 30, 40, 50]
        k = 5
        expectedOutcome = 10
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test9_large_numbers(self):
        nums = [10000, 50000, 100000, 75000, 25000]
        k = 2
        expectedOutcome = 75000
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test10_duplicate_kth_largest(self):
        nums = [1, 2, 2, 2, 3, 4, 5, 6]
        k = 5
        expectedOutcome = 2
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

    def test11_large_input(self):
        nums = list(range(1, 100001))  # 1 to 100000
        k = 99999
        expectedOutcome = 2
        self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

if __name__ == '__main__':
    unittest.main()

