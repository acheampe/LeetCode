from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        return intervals as an array after inserting newInterval without any overlaps

        Args: List of intervals; a new interval to be inserted

        Output: New lists of intervals after merging new interval without overlap

        Time Complexity: O(n)
        Space Complexity: Worst case O(n) if no merges
        """

        ### Another example of seperation of concerns to solve problem ###
        # Edge Case
        if not intervals or not intervals[0]:
            return [newInterval]
        
        # establish memory needed for operation
        resultIntervals = [] # our return list

        for i in range(len(intervals)):

            # if current interval in before newInterval
            if intervals[i][1] < newInterval[0]:
                resultIntervals.append(intervals[i])
            
            # if current Interval is after newInterval
            elif intervals[i][0] > newInterval[1]:
                resultIntervals.append(newInterval)

                return resultIntervals + intervals[i:]
            
            else: # merging concern
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # if new interval is at the end:
        resultIntervals.append(newInterval)

        return resultIntervals


sol = Solution()

# Basic cases
print(sol.insert([[1,3],[6,9]], [2,5]))  # Expected: [[1,5],[6,9]]
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Expected: [[1,2],[3,10],[12,16]]

# Edge case: empty intervals
print(sol.insert([], [5,7]))  # Expected: [[5,7]]

# Edge case: inserting at the beginning without overlap
print(sol.insert([[3,6],[8,10]], [1,2]))  # Expected: [[1,2],[3,6],[8,10]]

# Edge case: inserting at the end without overlap
print(sol.insert([[1,3],[6,9]], [10,12]))  # Expected: [[1,3],[6,9],[10,12]]

# Edge case: inserting at the beginning with merging
print(sol.insert([[3,6],[8,10]], [1,4]))  # Expected: [[1,6],[8,10]]

# Edge case: inserting at the end with merging
print(sol.insert([[1,3],[6,9]], [8,12]))  # Expected: [[1,3],[6,12]]

# Edge case: inserting in the middle, merging with two intervals
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [5,9]))  # Expected: [[1,2],[3,10],[12,16]]

# Edge case: new interval fully contains existing intervals
print(sol.insert([[2,3],[5,7]], [1,10]))  # Expected: [[1,10]]

# Edge case: inserting an interval that exactly matches an existing interval
print(sol.insert([[1,5],[6,9]], [1,5]))  # Expected: [[1,5],[6,9]]

# Edge case: inserting an interval that slightly extends an existing interval
print(sol.insert([[1,3],[6,9]], [2,6]))  # Expected: [[1,9]]

# Edge case: inserting an interval that spans multiple existing intervals
print(sol.insert([[1,3],[4,6],[7,9]], [2,8]))  # Expected: [[1,9]]

# Edge case: inserting an interval that exactly fits between two existing intervals
print(sol.insert([[1,2],[5,6]], [3,4]))  # Expected: [[1,2],[3,4],[5,6]]

# Edge case: inserting an interval that slightly overlaps at the edges
print(sol.insert([[1,3],[6,9]], [3,6]))  # Expected: [[1,9]]

# Edge case: inserting an interval that spans the entire existing intervals
print(sol.insert([[2,3],[4,5],[6,7]], [1,8]))  # Expected: [[1,8]]