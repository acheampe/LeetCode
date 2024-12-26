from typing import List

class Solution: # TC O(n log n) . SC O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Return array of non-overlapping intervals
        """

        if not intervals:
            return []
        
        # Sort interval list by it starting index
        intervals.sort(key=lambda x: x[0])

        resultIntervals = [intervals[0]]

        for i in range(1, len(intervals)):

            # To retrieve last interval
            lastInterval = resultIntervals[-1]

            # compare current 0 val to previous 1 val
            if intervals[i][0] <= lastInterval[1]:
                lastInterval[1] = max(lastInterval[1],intervals[i][1])
            
            # Append current interval
            else:
                resultIntervals.append(intervals[i])
        
        return resultIntervals

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]])) # [[1,5]]
