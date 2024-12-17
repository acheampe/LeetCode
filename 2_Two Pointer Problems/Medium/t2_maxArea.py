from typing import List

# Time Complexity == O(n) and Space Complexity == O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Return the maximum amount of water a container can store.   
        """

        startPointer, endPointer = 0, len(height) - 1
        maxArea = 0

        while startPointer < endPointer:
            
            # Calc. current max allowable height and length
            currMinHeight = min(height[startPointer], height[endPointer])
            currLength = endPointer - startPointer

            maxArea = max(maxArea, currMinHeight * currLength)

            if height[startPointer] > height[endPointer]:
                endPointer -=1
            elif height[startPointer] < height[endPointer]: 
                startPointer += 1
            
            else:
                startPointer += 1
                endPointer -=1 

        
        return maxArea

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # Expected: 49
print(sol.maxArea([1,1])) # Expected: 1

        