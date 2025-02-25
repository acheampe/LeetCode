from typing import List
import heapq
from collections import defaultdict
import unittest

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Returns an array of the median in each sliding window of size k.
        
        Time Complexity: O(n log k) using two heaps.
        Space Complexity: O(k).
        """
        
        # Max heap (stores negative values to simulate max heap)
        leftHalf = []
        # Min heap (stores larger half)
        RightHalf = []
        # Dictionary to track numbers to be lazily removed
        toRemove = defaultdict(int)
        # List to store medians
        medianCollection = []

        # add initial window to heap
        for i in range(k):
            if len(leftHalf) == len(RightHalf):
                heapq.heappush(leftHalf, -heapq.heappushpop(RightHalf, nums[i])) # maintain balance with value insertion (more efficent as well - O(log k))
            
            else:
                heapq.heappush(RightHalf, -heapq.heappushpop(leftHalf, -nums[i]))
        
        # add median in initial window
        medianCollection.append(float(-leftHalf[0]) if k & 1 else (RightHalf[0] + (-leftHalf[0])) / 2.0)

        # iterate through rest of num array and push to heap accordingly
        for j in range(k, len(nums)):
            heapq.heappush(leftHalf, -heapq.heappushpop(RightHalf, nums[j])) # maintain balance with added inbound value

            outBoundVal = nums[j - k]
            toRemove[outBoundVal] += 1 # marked for lazy removal

            if outBoundVal > -leftHalf[0]: # to maintain balance
                heapq.heappush(RightHalf, -heapq.heappop(leftHalf))
            
            # Lazy remove process
            while leftHalf and toRemove[-leftHalf[0]] > 0:
                toRemove[-leftHalf[0]] -= 1
                heapq.heappop(leftHalf)

            while RightHalf and toRemove[RightHalf[0]] > 0:
                toRemove[RightHalf[0]] -= 1
                heapq.heappop(RightHalf)

            # add median in initial window
            medianCollection.append(float(-leftHalf[0]) if k & 1 else (RightHalf[0] + (-leftHalf[0])) / 2.0)
    
        return medianCollection
    
    def solutionApproach(self):
        """
        This problem was a challenge to address (for me) even with an optimal
        approach.

        Utilizing two heap (a minHeap and maxHeap) is the way to go.

        First establish space for min and max heap operation. Followed by declaring 
        an array to collect the median in each k window and dictionary for 
        lazy removal. write a function that 
        returns the median val, calculated base on if k is Even or Odd.

        From here iterate through the first window k, to add to max_heap through 
        heappushpop on min_heap if length of both heaps are equal. This step is
        very important to increase efficiency (reposition ones) and maintains balance
        between min and max Heap. After append the function that returns the median 
        to our result collection.

        From here we iterate from k to end of input nums, then add to heappush max_heap
        through indirectly adding to heappushpop(min_heap, nums[i]) for balance.

        We then determine our out of window number (i -k) to add to lazy removal
        dictionary

        prior to removing, it is important to compare the outnum to top of max_heap.
        if outnumber is greater, the it must be in min_heap and we pop min_heap to add the 
        popped val to the max_heap

        from here we can write our lazy removal function to remove outnum if it is top of
        maxHeap or minHeap and we decrement from lazy removal dictionary accordingly

        Then we call median function to calc. what the median is to add to our result collection

        At end of iteration we return our result collection.

        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
    
    def solutionApproach2(self):
        """
        This problem was challenging to address optimally, even with the correct approach.

        The optimal way to solve it is by using **two heaps**:
        - **Max heap (leftHalf):** Stores the smaller half of numbers (negated values to simulate max heap).
        - **Min heap (RightHalf):** Stores the larger half of numbers.

        🚀 **Steps to solve the problem efficiently:**
        
        1️⃣ **Initialize Data Structures**  
        - Create `leftHalf` (max heap), `RightHalf` (min heap).
        - Use a `medianCollection` array to store median values.
        - Use a `toRemove` dictionary for **lazy removal**.

        2️⃣ **Process the First Window (`k` elements)**  
        - Insert numbers into heaps while **maintaining balance** using `heappushpop()`, 
            which **rebalances efficiently in O(log k)**.
        - If both heaps are equal in size, push to `maxHeap` via `heappushpop(minHeap)`.
        - Otherwise, push to `minHeap` via `heappushpop(maxHeap)`.
        - Compute the first median and add it to `medianCollection`.

        3️⃣ **Process Sliding Windows (`k` to `len(nums)`)**  
        - Insert **incoming number** into heaps using `heappushpop()` to maintain balance.
        - Identify **outgoing number (`nums[i - k]`)** and mark it for lazy removal in `toRemove`.
        - **Heap Adjustment:**  
            - If `outgoing number > top of maxHeap`, it must be in minHeap.  
            ✅ **Rebalance:** Remove from `minHeap` and push to `maxHeap`.  
        - **Lazy Removal:** Remove elements only when they reach the **top of a heap**.
        - Compute the median and append to `medianCollection`.

        4️⃣ **Return `medianCollection` after processing all sliding windows.**

        🔹 **Key Learnings:**
        - **Using `heappushpop()` minimizes unnecessary heap operations.**
        - **Checking if the outgoing number is greater than `maxHeap[0]` ensures balance.**
        - **Lazy removal avoids O(n) operations by deferring element deletions.**

        ⏳ **Time Complexity:** O(n log k)  
        🏗 **Space Complexity:** O(k)
        """

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

        # Test case 2: Another example from the problem statement
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