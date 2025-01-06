from typing import List

class Solution: # Time Complexity O(n), and Space Complexity = O(n) if considering result array
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert newInterval so that arr has no overlaps
        """

        # Edge case: 0 <= intervals.length <= 104
        if not intervals or not intervals[0]:
            return [newInterval]
        
        # Needed variables:
        resultIntervals = [] # O(n) space to return new upated arr
        currIndex, arrLen = 0, len(intervals)

        # Step 1 - Append all appropriate intervals before newInterval
        while currIndex < arrLen and intervals[currIndex][1] < newInterval[0]:
            resultIntervals.append(intervals[currIndex])
            currIndex += 1
        
        # Step 2 - Merge newInterval within appropriate intervals
        while currIndex < arrLen and newInterval[1] >= intervals[currIndex][0]:
            # Decide the min of starti
            newInterval[0] = min(newInterval[0], intervals[currIndex][0])        
            # Decide the max of endi
            newInterval[1] = max(newInterval[1], intervals[currIndex][1])

            currIndex += 1

        # Append the new Intervals
        resultIntervals.append(newInterval)  

        # Append rest of intervals
        resultIntervals.extend(intervals[currIndex : ])

        return resultIntervals
        

sol = Solution()
print(sol.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
# print(sol.insert([[]], [5, 7])) # [[1,2],[3,10],[12,16]]