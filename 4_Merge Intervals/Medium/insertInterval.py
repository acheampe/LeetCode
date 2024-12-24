from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert a new interval and merge if necessary.
        """
        resultIntervals = []

        # Edge case: If intervals is empty
        if not intervals or not intervals[0]:
            return [newInterval]

        for i in range(len(intervals)):
            # If the current interval is completely before the new interval
            if intervals[i][1] < newInterval[0]:
                resultIntervals.append(intervals[i])
            # If the current interval is completely after the new interval
            elif intervals[i][0] > newInterval[1]:
                resultIntervals.append(newInterval)
                # Add the rest of the intervals and return early
                return resultIntervals + intervals[i:]
            # Overlapping intervals, merge them
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # Add the merged interval at the end
        resultIntervals.append(newInterval)

        return resultIntervals


sol = Solution()
# print(sol.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
# print(sol.insert([[]], [5, 7])) # [[1,2],[3,10],[12,16]]