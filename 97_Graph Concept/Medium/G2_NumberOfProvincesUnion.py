from typing import List
import unittest

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Return the number of provinces using the Disjoint Set (Union-Find) approach.

        Time Complexity: nearly O(n) == O(n alpha(n))

        Space Complexity: O(n), due to established space for parent
        """
        
        # Establish space needed for operation
        parent = [i for i in range(len(isConnected))]
        
        # Find head parent with path compression
        def find(city): # nearly O(1) 0peration

            if parent[city] != city:

                parent[city] = find(parent[city])
            
            return parent[city]
        
        # Merge two sets that are connected
        def union(city1, city2):

            root1 = find(city1)
            root2 = find(city2)
            
            if root1 != root2: # different sets
                parent[root2] = root1 # merge into one set
        
        # iterate and process through adjacent list:
        for i in range(len(isConnected)):

            for j in range(i + 1, len(isConnected)): # only checks upper bound, avoids redundancy

                if isConnected[i][j] == 1:
                    union(i, j)
        
        province = set()
        # count and return unique roots as distinct provinces
        for i in range(len(isConnected)):
            province.add(find(i))
            
        return len(province)


class TestFindCircleNum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        outPut = 2
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test2(self):
        isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        outPut = 3
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test3(self):  # Single city (Minimum Constraint)
        isConnected = [[1]]
        outPut = 1
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test4(self):  # Fully connected cities (One province) 
        isConnected = [[1,1,1],[1,1,1],[1,1,1]]
        outPut = 1
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test5(self):  # Large n with a single province (Fully connected) 
        isConnected = [[1]*10 for _ in range(10)]
        outPut = 1
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test6(self):  # Large n with no connections (Each city is its own province)
        isConnected = [[1 if i == j else 0 for j in range(10)] for i in range(10)]
        outPut = 10
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test7(self):  # Multiple small provinces
        isConnected = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,1,0],
            [0,0,1,1,0],
            [0,0,0,0,1]
        ]
        outPut = 3
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test8(self):  # Complex province structure
        isConnected = [
            [1,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,1,1,0,0,0],
            [0,0,0,1,1,0],
            [0,0,0,1,1,1],
            [0,0,0,0,1,1]
        ]
        outPut = 2
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    def test9(self):  
        import random
        n = 50
        isConnected = [[1 if i == j or random.random() < 0.05 else 0 for j in range(n)] for i in range(n)]
        # Output is unknown but ensures performance on large inputs.
        self.assertIsInstance(self.sol.findCircleNum(isConnected), int)

if __name__ == '__main__':
    unittest.main()