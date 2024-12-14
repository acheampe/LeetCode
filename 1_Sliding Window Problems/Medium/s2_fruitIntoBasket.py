from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        return the max number of subarr length of tree of two types
        """

        # Initial Variables
        typeCounter = 0  # track unique counts
        leftIndex, rightIndex = 0, 0
        fruitTracker = set()
        maxRowLength = 0
        currRowLength = 0

        if len(fruits) == 1:
            return 1 # only one option 
        
        while rightIndex < len(fruits):
            #track fruit type and counter
            if fruits[rightIndex] not in fruitTracker:
                fruitTracker.add(fruits[rightIndex])
                while rightIndex < len(fruits) and fruits[rightIndex] in fruitTracker:
                    rightIndex += 1
                typeCounter = len(fruitTracker)
            
            else:
                rightIndex += 1
            
            while typeCounter >= 2:
                # Track length after type counter == 2
                if typeCounter == 2:
                    currRowLength = max(currRowLength, (rightIndex) - leftIndex)
                    maxRowLength = max(maxRowLength, currRowLength)
            
                # Track leftIndex 
                removeFruit = fruits[leftIndex]
                while fruits[leftIndex] == removeFruit:
                    leftIndex += 1
                    # Increment left Index and decrement typeCounter
                    if fruits[leftIndex] != removeFruit:
                        fruitTracker = set()
                        typeCounter = 0
            
                # Jump left index, Add current fruit to tracker and increment count
                leftIndex = rightIndex - 1
                fruitTracker.add(fruits[leftIndex])
                typeCounter = len(fruitTracker)
            
        return maxRowLength



        
                
sol = Solution()
print(sol.totalFruit([1,2,1])) # Expected: 3
print(sol.totalFruit([0,1,2,2])) # Expected: 3
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # Expected: 5