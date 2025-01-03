from typing import List
from collections import defaultdict

class Solution:  # Space Complexity = O(k), k = 2; Time Complexity = O(n)
    def totalFruit(self, fruits: List[int]) -> int:
        """
        return the max number of subarr length of tree of two types
        """

        # SOLVED BUT MISUNDERSTOOD THE QUESTION...you can only travel right, no circling back!

        # Edge Case:
        if len(fruits) <= 2:
            return len(fruits)
        
        # Variables needed to track fruits and max return
        maxNumber = float('-inf')
        left, right = 0, 1 # for sliding window reduction
        n = len(fruits) # length of array
        fruitType = defaultdict(int)
        fruitType[fruits[left]] += 1 # count first fruitType

        # Sliding Window expansion concern
        while left % n < right % n:
            fruitType[fruits[right % n]] += 1
            right += 1

            # reduction concern
            while len(fruitType) > 2:
                fruitType[fruits[left % n]] -= 1

                # remove type if 0
                if fruitType[fruits[left % n]] == 0:
                    del fruitType[fruits[left % n]]
                
                left += 1
            
            # Track max return
            currTotal = 0
            for fruit in fruitType.keys():
                currTotal += fruitType[fruit]
            
            maxNumber = max(maxNumber, currTotal)

        return maxNumber

    
      
sol = Solution()
# print(sol.totalFruit([1,2,1])) # Expected: 3
# print(sol.totalFruit([0,1,2,2])) # Expected: 3
# print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # Expected: 5
# print(sol.totalFruit([1,1])) # Expected: 2
# print(sol.totalFruit([6,6,6,6,6,6])) # Expected: 6
# print(sol.totalFruit([3,1,3,2,2])) # Expected: 4
