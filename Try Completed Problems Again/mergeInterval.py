from typing import List

class Solution: # TC O(n log n) SC O(1)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Return array of non-overlapping intervals
        """

        lenArr = len(intervals)

        # Step 1: Edge case of length or intervals = 1
        if lenArr == 1:
            return intervals

        # Step 2: Sort array first before merging appropriate intervals[-]
        intervals.sort(key=lambda x: x[0]) # sort by key val

        # Step 3: Parse through array and sort when appropriate
        currIndex = 0
        while currIndex < lenArr - 1:

            # Continue conditions:
            if intervals[currIndex][1] < intervals[currIndex + 1][0]:
                currIndex += 1
            
            else:

                # Merge condition
                while currIndex < lenArr - 1 and intervals[currIndex][1] >= intervals[currIndex + 1][0]:
                    intervals[currIndex][0] = min(intervals[currIndex][0], intervals[currIndex + 1][0])
                    intervals[currIndex][1] = max(intervals[currIndex][1], intervals[currIndex + 1][1])

                    # del currIndex + 1
                    del intervals[currIndex + 1]

                    # reset len of arr
                    lenArr = len(intervals)
        
        return intervals


sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]])) # [[1,5]]


# from typing import List

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         """
#         Merge overlapping intervals and return a list of non-overlapping intervals.
#         """
#         # Step 1: Sort intervals by their start time
#         intervals.sort(key=lambda x: x[0])  # O(n log n)

#         # Step 2: Initialize the result array
#         result = [intervals[0]]  # Start with the first interval

#         # Step 3: Merge intervals
#         for i in range(1, len(intervals)):
#             # Get the last interval in the result
#             lastInterval = result[-1]

#             # Check if the current interval overlaps with the last interval
#             if intervals[i][0] <= lastInterval[1]:
#                 # Merge the intervals
#                 lastInterval[1] = max(lastInterval[1], intervals[i][1])
#             else:
#                 # Add the current interval as a new non-overlapping interval
#                 result.append(intervals[i])

#         return result
