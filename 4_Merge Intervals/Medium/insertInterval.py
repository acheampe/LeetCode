from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert a new interval and merge if necessary.
        """

        if not intervals or not intervals[0]:
            return newInterval
        
        resultIntervals = []

        # Iterate through range
        for i in range(len(intervals)):

            # if current interval is before new Interval
            if intervals[i][1] < newInterval[0]:
                resultIntervals.append(intervals[i])
            
            # if current interval is after new Interval
            elif intervals[i][0] > newInterval[1]:
                resultIntervals.append(newInterval)

                # append rest of intervals for early return 
                return resultIntervals + intervals[i:]
            
            else: # Merge scenarios
                # find min of newInterval
                newInterval[0] = min(newInterval[0], intervals[i][0])
                # find max of newInterval
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # Add new interval to the end if not merged or integrated at this point
        resultIntervals.append(newInterval)

        return resultIntervals


sol = Solution()
# print(sol.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
# print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
# print(sol.insert([[]], [5, 7])) # [[1,2],[3,10],[12,16]]