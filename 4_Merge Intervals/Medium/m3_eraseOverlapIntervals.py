from typing import List

class Solution: # TC O(n log n) . SC O(n)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        return the minimum number of intervals you need to remove to make the 
        rest of the intervals non-overlapping.
        """

        # Step 1: Edge case of length 1
        if len(intervals) == 1:
            return 0 # no overlaps
        
        # Step 2: Variable track min overlaps and sort intervals
        minOverLaps = 0
        prevIndex, currIndex = 0, 0
        intervals.sort(key=lambda x: x[0]) # Introduces Complexity of O(n long n)
        
        while currIndex < len(intervals):
            currIndex += 1

            while currIndex < len(intervals) and intervals[currIndex] == intervals[prevIndex]: 
                # Count overlap
                minOverLaps += 1
                currIndex += 1

            prevIndex = currIndex - 1
            tempCount = 0 # count current overlaps with previous index
            while currIndex < len(intervals) and intervals[currIndex][0] < intervals[prevIndex][1]:
                tempCount += 1
                currIndex += 1
                prevIndex += 1

            if tempCount > 0:
                minOverLaps += 1
                prevIndex = currIndex
                

        return minOverLaps




sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # Expected Output: 1
print(sol.eraseOverlapIntervals([[1,2],[1,2],[2,3],[3,4],[1,3],[3,4]])) # Expected Output: 3
print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
print(sol.eraseOverlapIntervals([[1,2],[2,3]])) # 0
