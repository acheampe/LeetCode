from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        return interval in place with no overlaps"
        """

        # Edge case of intervals.length <= 0:
        if not intervals:
            return newInterval# return new intervals as is due to empty arr
        
        # Address condition for when startIndex = 0 and newInterval should be placed before it
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval) # results in O(n)
            return intervals

        # Address condition when newInterval should be place after intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals
        
        # Needed Variables for core logic:
        startIndex, endIndex = 0, len(intervals) - 1 # exclusive of last interval

        while startIndex < endIndex:

            # Condition for perfect placement without merging:
            if newInterval[0] > intervals[startIndex][1] and newInterval[1] < intervals[startIndex][0]:
                intervals.insert(startIndex + 1, newInterval) # Worse case: O(n)
                return intervals
            
            # Merge condition:
            while newInterval[0] <= intervals[startIndex][1]:
                
                mergeIndex = startIndex
                # condition to take care of start values of intervals <= newInterval[0]
                if newInterval[0] <= intervals[startIndex][0]:
                    intervals[mergeIndex][0] = newInterval[0]
                
                    if newInterval[1] > intervals[startIndex][1] and newInterval[1] < intervals[startIndex + 1][0]:
                        intervals[mergeIndex][1] = newInterval[1]
                        return intervals
                    
                    startIndex += 1
                    while intervals[startIndex][0] < newInterval[1] and intervals[startIndex][1] < newInterval[1] :
                        del intervals[startIndex]
                    
                    if newInterval[1] < intervals[startIndex][0]:
                        intervals[mergeIndex][1] = newInterval[1]
                        return intervals
                    
                    else:
                        intervals[mergeIndex][1] = intervals[startIndex][1]
                        return intervals




            
        


sol = Solution()
print(sol.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
# print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
# print(sol.insert([[]], [5, 7])) # [[1,2],[3,10],[12,16]]