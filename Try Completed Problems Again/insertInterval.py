from typing import List

class Solution: # Time Complexity O(n), and Space Complexity = O(n) if considering result array
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        return interval in place with no overlaps"
        """

        # Edge case of intervals.length <= 0:
        if not intervals or not intervals[0]:
            return newInterval # return new intervals as is due to empty arr
        
        # result intervals are appended here
        resultInterval = []

        # Basic variables needed for rest of operation
        currIndex = 0
        arrLen = len(intervals)

        # First, take case of all intervals before having the need to merge
        while currIndex < arrLen and intervals[currIndex][1] < newInterval[0]:
            resultInterval.append(intervals[currIndex])
            currIndex += 1
        
        # Second Merge condition
        while currIndex < arrLen and intervals[currIndex][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[currIndex][0])
            newInterval[1] = max(newInterval[1], intervals[currIndex][1])

            currIndex += 1
        
        # Third, Append merged intervals
        resultInterval.append(newInterval)

        # Fourth, Append rest of the intervals
        resultInterval.extend(intervals[currIndex:])

        return resultInterval

sol = Solution()
print(sol.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
# print(sol.insert([[]], [5, 7])) # [[1,2],[3,10],[12,16]]