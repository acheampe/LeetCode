from typing import List

class Solution: # TC O(n log n) SC O(1)
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
        intervals.sort(key=lambda x: x[0]) # Introduces Complexity of O(n long n)
        currFixedInterval = intervals[0]
        currIndex = 1

        while currIndex < len(intervals):

            # Step 3: check if intervals are equal 
            if intervals[currIndex] == currFixedInterval:
                minOverLaps += 1
                currIndex += 1

            # Step 4: check if there is an overlap between fixed val and iter val
            elif intervals[currIndex][0] < currFixedInterval[1]:

                # assign the lesser of end interval to current fixed
                currFixedInterval = intervals[currIndex] if intervals[currIndex][1] \
                < currFixedInterval[1] else currFixedInterval
                minOverLaps += 1
                currIndex += 1

            else:
                # Step 5: update fixInterval if no overlap
                currFixedInterval = intervals[currIndex]
                currIndex += 1
        

        return minOverLaps




sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # Expected Output: 1
print(sol.eraseOverlapIntervals([[1,2],[1,2],[2,3],[3,4],[1,3],[3,4]])) # Expected Output: 3
print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
print(sol.eraseOverlapIntervals([[1,2],[2,3]])) # 0
