from typing import List
import unittest
import heapq

import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        Returns the smallest range that includes one number from each of the 
        k lists

        Args: nums --> List[lists]

        Return: list, containing the smallest range.
        """

        # Edge case: There will always be at least one k
        if len(nums) == 1:
            return [nums[0][0], nums[0][0]] # no further iteration needed
        
        # Establish need variables/space for operation
        minHeap = []
        minRange = float('inf')
        resultRange = [0, 0] # return min range
        currMax = float('-inf')

        for listIndex in range(len(nums)):
            
            # update currMax within minHeap range
            currMax = max(currMax, nums[listIndex][0])
            heapq.heappush(minHeap, (nums[listIndex][0], listIndex, 0)) # contains (arr val, list index position, index of curr val of curr list)
        
        # iterate through min_heap to find minRange
        while minHeap:

            currVal, listIndex, arrIndex = heapq.heappop(minHeap)

            # Calc current minRange
            currRange = currMax - currVal

            # check to see if update to minRange is needed
            if currRange <= minRange:

                if currRange < minRange:
                    # update return range and minRange
                    resultRange = [currVal, currMax]

                else: # if equal, return the range with the lesser startindex
                    if currVal < resultRange[0]:
                        resultRange = [currVal, currMax]

                minRange = currRange
            
            if arrIndex + 1 < len(nums[listIndex]):
                
                # push new val to minHeap
                heapq.heappush(minHeap, (nums[listIndex][arrIndex + 1], listIndex, arrIndex + 1))

                # update currMax
                currMax = max(currMax, nums[listIndex][arrIndex + 1])
            
            else:
                return resultRange
        
        return resultRange


    def approachSolution(self):
        """
        The best way to approach this problem, and any problem regarding kth-somthing
        is through a heap data structure. 

        First thing to consider is to make sure that list and all the list within 
        the list is not empty

        After, we want to add the first index of each list within the array to a min_heap, 
        while tracking which of the k_list has the max value. Tracking max here will simplify our
        approach

        we also want to track what our min_range is

        from here, we initiate while min_heap, and heappop or min value, calculate
        the min difference with our max Value and update or range if min is lower

        Then we heappush the next value from the list that we we just popped of min_heap,
        update our max value if needed with the value that we will push, and repeat. 

        we will go through this while cycle till min_heap is false and then simply return 
        the minRange that we found through the iteration as a list
        """
class TestSmallestRange(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Test case from example 1."""
        nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        expected_output = [20,24]
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_example_2(self):
        """Test case from example 2."""
        nums = [[1,2,3],[1,2,3],[1,2,3]]
        expected_output = [1,1]
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_single_list(self):
        """Only one list is provided, the range should be the smallest possible."""
        nums = [[1,2,3,4,5]]
        expected_output = [1,1]  # The smallest range containing at least one number from all lists is a single number.
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_two_lists_with_overlap(self):
        """Two lists with overlapping elements."""
        nums = [[1,5,10],[4,6,12]]
        expected_output = [4,5]  # The smallest range that includes at least one number from both lists.
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_two_lists_no_overlap(self):
        """Two lists with no overlapping elements."""
        nums = [[1,2,3],[10,11,12]]
        expected_output = [3,10]  # The smallest possible range to include at least one number from each list.
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_lists_with_large_numbers(self):
        """Lists containing large numbers to ensure solution handles extreme values."""
        nums = [[10**5-2, 10**5-1, 10**5],[10**5-3, 10**5-2, 10**5-1]]
        expected_output = [10**5-2, 10**5-2]  # Smallest range that includes all lists.
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_smallest_possible_case(self):
        """Minimum input case with k=1 and one element."""
        nums = [[7]]
        expected_output = [7,7]
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_all_lists_with_same_elements(self):
        """Every list contains the exact same numbers."""
        nums = [[2,2,2],[2,2,2],[2,2,2]]
        expected_output = [2,2]  # The smallest range is a single number.
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

    def test_lists_with_different_lengths(self):
        """Lists of varying lengths should still find the smallest range."""
        nums = [[1, 5, 10, 15], [2, 3, 4, 8, 12], [6, 9, 14]]
        expected_output = [4,6]  # The best range covering all lists.
        self.assertEqual(self.sol.smallestRange(nums), expected_output)

if __name__ == '__main__':
    unittest.main()