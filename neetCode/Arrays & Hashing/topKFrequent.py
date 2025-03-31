from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) ->list[int]:
        """
        we can use heap to improve performance but for purpose of practicing
        bruteforce and arrays we will solve this in O(n) TC and SC
        """

        # should I anticipate an empty array?
        # should I anticipate non-int values?
        
        countFrequency = Counter(nums)
        result = []
        
        while k > 0:
            curr = float('-inf')
            key = None
            for h, v in countFrequency.items():
                if curr < v:
                    curr, key = v, h
            result.append(key)
            del countFrequency[key]
            k -= 1
        
        return result

sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))
        
        