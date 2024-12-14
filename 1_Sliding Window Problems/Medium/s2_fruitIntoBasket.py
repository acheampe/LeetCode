from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        return the max number of subarr length of tree of two types
        """
        
        # Initiating variables

        maxSubArrLength, currSubArrLength = 0, 0
        leftIndex, rightIndex = 0, 0
        typeCounter = 0 # to track types of tree/fruit (2 types max)
        fruitTracker = set()
        rightIndex = 0
        fruitLength = len(fruits)

        # Iterate for loop for right index driver:
        while rightIndex < fruitLength:
            if fruits[rightIndex] not in fruitTracker:
                fruitTracker.add(fruits[rightIndex])
                typeCounter += 1

                currTree = fruits[rightIndex]
                while fruits[rightIndex] in fruitTracker and rightIndex < fruitLength:
                    if fruits[rightIndex] == currTree:
                        rightIndex += 1

                if typeCounter == 2:
                    # Track viable subarr lengths
                    currSubArrLength = rightIndex - leftIndex
                    maxSubArrLength = max(maxSubArrLength, currSubArrLength)

                    removeFruit = fruits[leftIndex]
                    
                    while leftIndex < rightIndex and fruits[leftIndex] == removeFruit:
                        leftIndex += 1

                    fruitTracker.remove(removeFruit)
                    typeCounter -= 1

        # update to max viable length
        maxSubArrLength = max(maxSubArrLength, currSubArrLength)
        
        return maxSubArrLength
            
                
sol = Solution()
# print(sol.totalFruit([1,2,1])) #Expected: 3
# print(sol.totalFruit([0,1,2,2])) #Expected: 4
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))