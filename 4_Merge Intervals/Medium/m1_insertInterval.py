from typing import List

class Solution: #TC = O(n)  SP = O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert a new interval and merge if necessary.
        """

        if not intervals or not intervals[0]:
            return [newInterval]
        
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


### Approach thought Process 

# Problem can seem initially daunting to address about when you take a step back #
# You realize that all you need is to seperate concerns to address the problem #
# First, is figuring out how to place all the intervals the comes before merging/inserting newInterval #
# Second, is figuring out the conditions that places all intervals after interval
# Lastly, is merging intervals when needed. This part can seem complicated but if you just
# update the min value of interval[0] and newInterval[0] in question and max value of 
# interval[1] and newInterval[1] in question, it will populate the desired output. 
