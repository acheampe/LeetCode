class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        return the min number of intervals to remove to make intervals 
        non-overlapping intervals
        
        TC: O(n log n) - for ordering array
        SC: O(1)
        """
        
        intervals.sort(key=lambda x:x[0]) # O(n log n)  operation
        counter = 0 # track min amount of intervals we must remove for non-overlap intervals
        endIndex, startIndex = len(intervals) - 1, 0
        
        #iterate backwards to increment count when we encounter valid overlap to remove
        while endIndex > startIndex:
            
            currIndex = endIndex - 1
            # address overlaps 
            while (currIndex > - 1) and (intervals[endIndex][0] < intervals[currIndex][1]):
                counter += 1
                currIndex -= 1
            
            endIndex = currIndex
                
        
        return counter

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # Expected Output: 1
print(sol.eraseOverlapIntervals([[1,2],[1,2],[2,3],[3,4],[1,3],[3,4]])) # Expected Output: 3
print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
print(sol.eraseOverlapIntervals([[1,2],[2,3]])) # 0