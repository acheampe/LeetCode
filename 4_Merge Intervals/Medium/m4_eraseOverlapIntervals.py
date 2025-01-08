from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Return the minimum number of intervals you need to remove to make the 
        rest of the intervals non-overlapping.
        """
        # Step 1: Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize variables
        minOverLaps = 0
        currEnd = float('-inf')  # End of the last non-overlapping interval

        # Step 3: Iterate through intervals
        for start, end in intervals:
            if start >= currEnd:
                # No overlap, update currEnd
                currEnd = end
            else:
                # Overlap detected, increment minOverLaps
                minOverLaps += 1

        return minOverLaps

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # Expected Output: 1
# print(sol.eraseOverlapIntervals([[1,2],[1,2],[2,3],[3,4],[1,3],[3,4]])) # Expected Output: 3
# print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
# print(sol.eraseOverlapIntervals([[1,2],[2,3]])) # 0