import unittest
from collections import defaultdict
import heapq

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """
        return Median of each subarray k in input array
        """

        maxHeap, minHeap = [], []
        collectMedians = []
        toRemove = defaultdict(int)

        for i in range(k):

            if len(maxHeap) == len(minHeap):
                heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, nums[i]))
            
            else:
                heapq.heappush(minHeap, -heapq.heappushpop(maxHeap, -nums[i]))
        
        collectMedians.append(float(-maxHeap[0]) if k & 1 else (minHeap[0] + (-maxHeap[0])) / 2.0)

        for j in range(k, len(nums)):

            # if len(maxHeap) == len(minHeap):
            heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, nums[j]))
            
            # find out of range val and add to hash
            outBound = nums[j - k]
            toRemove[outBound] += 1

            # balance for expecting removal of val from minHeap
            if outBound > -maxHeap[0]:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            
            # remove if conditions meet
            while maxHeap and toRemove[-maxHeap[0]] > 0:
                toRemove[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)
                
                
            while minHeap and toRemove[minHeap[0]] > 0:
                toRemove[minHeap[0]] -= 1
                heapq.heappop(minHeap)
                
            
            collectMedians.append(float(-maxHeap[0]) if k & 1 else (minHeap[0] + (-maxHeap[0])) / 2.0)
    
        return collectMedians
         
# class Solution:
#     def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
#         """return median array for each window in the original array"""
        
#         leftSide, rightSide = [], []  # maxHeap and minHeap respectively
#         lazyRemoval = defaultdict(int)
#         medianCollection = [] # collection of our median in each window
        
#         def calcMedian(maxHeap, minHeap):
            
#             if len(maxHeap) > len(minHeap):
#                 return -float(maxHeap[0])

#             return ((-maxHeap[0]) + minHeap[0]) / 2.0

#         def prune(heap):
#             """Pop elements marked for lazy removal from top of heap."""
#             while heap:
#                 num = -heap[0] if heap is leftSide else heap[0]
#                 if lazyRemoval[num] > 0:
#                     heapq.heappop(heap)
#                     lazyRemoval[num] -= 1
#                 else:
#                     break
        
#         def rebalance(): # balances tree when called upon
#             while len(leftSide) > len(rightSide) + 1:
#                 heapq.heappush(rightSide, -heapq.heappop(leftSide))
#                 prune(leftSide)
#             while len(rightSide) > len(leftSide):
#                 heapq.heappush(leftSide, -heapq.heappop(rightSide))
#                 prune(rightSide)
        
#         def addVal(num): # adds a value when called on
        
#             if len(leftSide) <= len(rightSide):
#                 heapq.heappush(leftSide, -heapq.heappushpop(rightSide, num))
#                 lazyRemoval[num] += 1 # track val frequency
            
#             else:
#                 heapq.heappush(rightSide, -heapq.heappushpop(leftSide, -num))
#                 lazyRemoval[num] += 1 # track val frequency              

#         for i, val in enumerate(nums):
        
#             if i < k: # initial window
#                 addVal(val)
            
#             else:
#                 medianCollection.append(calcMedian(leftSide, rightSide))
                
#                 addVal(val)
                
#                 outBoundVal = nums[i - k] 

#                 # initiate lazy removal
#                 if -leftSide[0] == outBoundVal and lazyRemoval[-leftSide[0]] > 0:
#                     lazyRemoval[-leftSide[0]] -= 1
#                     heapq.heappop(leftSide)
                    
#                 elif rightSide[0] == outBoundVal and lazyRemoval[rightSide[0]] > 0:
#                     lazyRemoval[rightSide[0]] -= 1 
#                     heapq.heappop(rightSide)

#                 rebalance()
        
#         return medianCollection
                
        
                    
    

# Unit Tests
class TestMedianSlidingWindow(unittest.TestCase):
    def test_median_sliding_window(self):
        solution = Solution()
        
        # Test case 1: Example from the problem statement
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected): 
            self.assertAlmostEqual(r, e, delta=1e-5)

        # # Test case 2: Another example from the problem statement
        nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
        k = 3
        expected = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 3: Single element in the array
        nums = [5]
        k = 1
        expected = [5.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 4: All identical elements
        nums = [2, 2, 2, 2, 2]
        k = 2
        expected = [2.00000, 2.00000, 2.00000, 2.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 5: Large array, k = 1
        nums = list(range(1, 1001))
        k = 1
        expected = [float(num) for num in nums]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 6: Large array, k = len(nums)
        nums = [1, 3, 2, 4]
        k = 4
        expected = [2.50000]  # Median of the entire array
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

if __name__ == '__main__':
    unittest.main()
    
