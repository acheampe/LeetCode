from typing import List
# TC == O(n) SC == O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        return indexes in order of its values that sums to targert
        """

        startIndex, endIndex = 0, len(numbers) - 1

        while startIndex < endIndex:
            
            currTotalVal = numbers[startIndex] + numbers[endIndex] 
            if currTotalVal == target:
                return [startIndex + 1, endIndex + 1]
            
            elif currTotalVal > target:
                endIndex -= 1
            
            else:
                startIndex += 1
        
        return []


        