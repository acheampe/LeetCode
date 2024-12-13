from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        return the maxLenSubArr of two-type tree/fruit to pick from
        """

        # Basic Variables
        maxLenSubArr = float('-inf')
        typeCounter = 1  # To track types of fruit (max 2)
        leftIndex = 0 
        rightIndex = 1
        typeFruit = set() # types of fruit in current Window
        typeFruit.add(fruits[leftIndex])

        # iterate through window: 
        while rightIndex < len(fruits):
            maxLenSubArr = max(maxLenSubArr, rightIndex - leftIndex)
            if fruits[rightIndex] not in typeFruit: 
                if typeCounter < 2:
                    typeFruit.add(fruits[rightIndex])
                    typeCounter += 1
                    
                else:
                    while fruits[leftIndex] in typeFruit:
                        typeFruit.remove(fruits[leftIndex])
                        leftIndex += 1
                        typeCounter -= 1 
                
            while rightIndex < len(fruits) and fruits[rightIndex] in typeFruit:
                    rightIndex += 1 if rightIndex < len(fruits) else rightIndex      

        return maxLenSubArr
                


sol = Solution()
# print(sol.totalFruit([1,2,1])) #Expected: 3
# print(sol.totalFruit([0,1,2,2])) #Expected: 4
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))