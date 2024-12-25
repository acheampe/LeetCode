from typing import List

# TC = O (n + m) and SC = O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead...Only in Leetcode
        """

        # Work array backwards
        i = m - 1 # end position of nums1 arr
        j = n - 1 # end position of nums2 arr
        k = m + n - 1 # last arr position of nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        
        # if there are some values left on nums1 arr
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        return nums1



sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # Expected [1,2,2,3,5,6]
print(sol.merge([1], 1, [], 0)) # Expected [1]
print(sol.merge([0], 0, [1], 1)) # Expected [1]
print(sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3)) # Expected [1,2,2,3,5,6]
print(sol.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)) # Expected [1,2,3,4,5,6]


