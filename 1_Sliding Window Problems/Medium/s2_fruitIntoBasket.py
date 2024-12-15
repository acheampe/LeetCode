from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        return the max number of subarr length of tree of two types
        """

        fruitTree = {}
        currRowLength, maxRowLength = 0, 0
        typeTracker = 0 # monitors length of dictionary
        leftIndex, rightIndex = 0, 0

        if len(fruits) == 1:
            return 1

        while rightIndex < len(fruits):
            # track and count tree types (types are keys, and amounts are the values)
            while typeTracker <= 2 and rightIndex <= len(fruits):
                if typeTracker == 2:
                    currRowLength = rightIndex - leftIndex 
                    maxRowLength = max(maxRowLength, currRowLength)
                    
                if rightIndex < len(fruits) and fruits[rightIndex] not in fruitTree:
                    fruitTree[fruits[rightIndex]] = 0
                
                if rightIndex != len(fruits):
                    fruitTree[fruits[rightIndex]] = 1 + fruitTree.get(fruits[rightIndex], 0)
                    typeTracker = len(fruitTree)
                    rightIndex += 1
                
                else:
                    return fruitTree[fruits[leftIndex]] if typeTracker == 1 else maxRowLength

            while typeTracker > 2:
                if fruitTree.get(fruits[leftIndex], 0) == 0:
                    del fruitTree[fruits[leftIndex]]
                    leftIndex += 1
                    typeTracker = len(fruitTree)
                
                else:
                    fruitTree[fruits[leftIndex]] -= 1
                    if fruitTree.get(fruits[leftIndex], 0) == 0:
                        del fruitTree[fruits[leftIndex]]
                        typeTracker = len(fruitTree)
                    leftIndex += 1
        
        return maxRowLength

    
      
sol = Solution()
# print(sol.totalFruit([1,2,1])) # Expected: 3
# print(sol.totalFruit([0,1,2,2])) # Expected: 3
# print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # Expected: 5
print(sol.totalFruit([1,1])) # Expected: 2
