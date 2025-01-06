from typing import List

class Solution:  # Time Complexity: O(n log n), Space Complexity: O(n)...
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sorting array using divide and conquer"""
        # Base/Termination case:
        if len(nums) <= 1:
            return nums

        # Division phase:
        middle = len(nums) // 2
        leftOrder = self.sortArray(nums[:middle])
        rightOrder = self.sortArray(nums[middle:])

        return self.orderHelper(leftOrder, rightOrder)

    def orderHelper(self, leftArr, rightArr):
        """Merge two sorted arrays into one sorted array"""
        orderedResult = []
        startLeft, startRight = 0, 0
        endLeft, endRight = len(leftArr), len(rightArr)

        while startLeft < endLeft and startRight < endRight:
            if leftArr[startLeft] <= rightArr[startRight]:
                orderedResult.append(leftArr[startLeft])
                startLeft += 1
            else:
                orderedResult.append(rightArr[startRight])
                startRight += 1

        # Extend remaining elements from leftArr or rightArr
        orderedResult.extend(leftArr[startLeft:])
        orderedResult.extend(rightArr[startRight:])
        return orderedResult

sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))  # Expected: [1, 2, 3, 5]
# print(sol.sortArray([5, 1, 1, 2, 0, 0]))  # Expected: [0, 0, 1, 1, 2, 5]
# print(sol.sortArray([-2, 3, -5]))  # Expected: [-5, -2, 3]

# IN PLACE SORT APPROACH TO LEARN FOR LEAST SPACE USED:
# from typing import List

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         """
#         In-place Merge Sort with O(1) additional space
#         """
#         def mergeSort(nums, left, right):
#             # Base case: single-element array is sorted
#             if left >= right:
#                 return

#             # Divide
#             mid = (left + right) // 2
#             mergeSort(nums, left, mid)
#             mergeSort(nums, mid + 1, right)

#             # Conquer: In-place merge
#             merge(nums, left, mid, right)

#         def merge(nums, left, mid, right):
#             i, j = left, mid + 1

#             # Use a pointer-based approach to merge two sorted halves
#             while i <= mid and j <= right:
#                 if nums[i] <= nums[j]:
#                     # Element in left half is in correct position
#                     i += 1
#                 else:
#                     # nums[j] is smaller, needs to be inserted before nums[i]
#                     value = nums[j]
#                     # Shift all elements in left half to make space for nums[j]
#                     for k in range(j, i, -1):
#                         nums[k] = nums[k - 1]
#                     nums[i] = value

#                     # Update pointers
#                     i += 1
#                     mid += 1
#                     j += 1

#         mergeSort(nums, 0, len(nums) - 1)
#         return nums