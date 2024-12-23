from typing import List

# TC = O (n2) and SC = O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead...Only in Leetcode
        """

        # Define start and end pos for both nums
        nums1Start, nums2Start = 0, 0

        # 1) while num2 iter has not ended @ m - 1:
        while nums2Start < n and nums1Start < m:
            if nums1[nums1Start] > nums2[nums2Start]:
                nums1[nums1Start], nums2[nums2Start] = nums2[nums2Start], nums1[nums1Start]
                nums1Start += 1

                if nums2Start <= n - 2 and nums2[nums2Start] > nums2[nums2Start + 1]:
                    while nums2Start + 1 < n and nums2[nums2Start] > nums2[nums2Start + 1]:
                        nums2[nums2Start], nums2[nums2Start + 1] = nums2[nums2Start + 1], nums2[nums2Start]
                        nums2Start += 1

                nums2Start = 0 

            # else
            else:
                # iter to next num1 val
                nums1Start += 1

    #2) Redefine variables
    #  startpos1 = endpos + 1
        nums1Start, nums1End = m, m + n 
    #  start2, end2 = 0
        nums2Start, nums2End = 0, n

    #3) Initiate another while loop
    # while startpos < endpos and start2 < end2:
        while nums1Start < nums1End and nums2Start < nums2End:
            nums1[nums1Start] = nums2[nums2Start]
            nums1Start += 1
            nums2Start += 1
        
        
        return nums1



sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # Expected [1,2,2,3,5,6]
print(sol.merge([1], 1, [], 0)) # Expected [1]
print(sol.merge([0], 0, [1], 1)) # Expected [1]
print(sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3)) # Expected [1,2,2,3,5,6]
print(sol.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)) # Expected [1,2,3,4,5,6]


