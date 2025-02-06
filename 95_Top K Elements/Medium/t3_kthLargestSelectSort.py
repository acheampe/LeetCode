from typing import List
import unittest

class Solution: # SELECT SORT APPROACH
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        returns the kths largest (not the kth distinct)

        Args: nums --> List; k --> int

        Return: int (the kths largest)

        Time Complexity = O(n) on average, worst O(n^2)
        Space Complexity = O(1)
        """

        return self.selectSort(nums, 0, len(nums) - 1, k)

    def partition(self, nums, low, high):
        """
        partition to find appropriate index of pivot

        Time Complexity: Average - O(n), worst case O(n^2) if pivot is the smallest or largest val
        Space Complexity: O(1)
        """
        # values to find pivot position
        pivot = high 
        i = low - 1 

        for j in range(low, high): # maintain actual boundary though exclusive in this loop
            
            # if j value is less/equal to pivot val
            if nums[j] <= nums[pivot]:
                i += 1 # increment index val

                # switch values -- > this makes sure that all vals less/== to pivot val
                # is place to the left of i index (partition index)
                nums[i], nums[j] = nums[j], nums[i] 
            
        # To place pivot val in it's appropriate index
        nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1] # +1 considers last array val

        return i + 1  # returns pivot index
        
    def selectSort(self, nums, low, high, k):
        """
        Use select sort to find desired kth largest
        """

        # Establish index to return on:
        desiredIndex = len(nums) - k
        # Find pivot:
        index = self.partition(nums, low, high)

        if index == desiredIndex:
            return nums[index] # we have found our kth largest
        
        # To search left side
        elif desiredIndex < index:
            return self.selectSort(nums, low, index - 1, k)
        
        else:
            return self.selectSort(nums, index + 1, high, k)
    
    def approachSolution(self):
        """
        Utilizing select sort approach for this problem is a viable option if 
        dataset is small, ideally less than 10^6...for large dataset, consider
        min_heap approach

        To solve this question optimally with select sort strategy, we much strategically
        separate functions to own one responsibility.

        First, we must create a partition function that will strictly be within 
        viable Inclusive boundaries. 

        Then define our pivot, most commonly by selecting the last index (do note that
        this has it's inconveniece if pivot is the largest or smallest value). 
        From here we initiate a partition index at -1 and then iterate a for loop
        through our our current array window. if current iteratio is less than or equal
        to pivot val we perform a switch value with current index and partition index to allow
        all values less than or equal pivot to be on its left.

        This will occur till end of our iteration then we perform a switch between 
        partition + 1 index with pivot and then return partition + 1 index.

        At this point we should no the kth index (len(arr) - k).

        We then create a select sort function that will compare if we have found our 
        index, if not, we recursively call selectsort if or desired index is to the right or left, with
        its appropriate boundaries, that will initiate the partition again, till select sort returns 
        or desired value.

        This approach is space efficient O(1) and Time complexity is O(n)

        sticky situation:
        The point of difficulty i encountered was due to trying to be smart with my partition boundaries during 
        for loop iteration. I figured all i have to return is i if range is from (low to high + 1) but this introduced
        unneed difficulty. KISS - Keep it simple stupid. stick with the inclusive range (low to high) and at then end of loop
        juft return partition index + 1 after switching thier vals with pivot val to avoid introducing bugs or complications. 
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

    # def test11_large_input(self): # Select Sort approach will trigger TLE due to large input (use min_heap instead)
    #     nums = list(range(1, 100001))  # 1 to 100000
    #     k = 99999
    #     expectedOutcome = 2
    #     self.assertEqual(self.sol.findKthLargest(nums, k), expectedOutcome)

if __name__ == '__main__':
    unittest.main()