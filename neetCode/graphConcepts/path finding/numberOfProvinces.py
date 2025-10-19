import unittest

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # Time Complexity (TC): O(n^2)
        # - O(n^2) to build the adjacency list from the isConnected matrix
        # - O(n^2) to traverse all nodes and edges in the worst case (fully connected graph)

        # Space Complexity (SC): O(n^2)
        # - O(n^2) for the adjacency list in the worst case
        # - O(n) for the recursion stack and sets (seenCity and currPath)
        
        seenCity: set[int] = set()
        countProvince: int = 0
        adjListGraph = {}
        m, n = len(isConnected), len(isConnected[0])
        
        for i in range(m):
            adjListGraph[i + 1] = []
            for j in range(n):
                
                if i != j and self.isEdgeCity(i, j, isConnected): 
                    adjListGraph[i + 1].append(j + 1)
                
        def isProvince(city: int, currPath: set) -> bool:
            
            if city in currPath:
                return False 
            
            currPath.add(city)
            
            for nei in adjListGraph[city]:
                isProvince(nei, currPath)
                
            currPath.remove(city)
            seenCity.add(city)
            
            return True
        
        for key in adjListGraph.keys():
            currentProvince: set = set()
            if key not in seenCity and isProvince(key, currentProvince):
                countProvince += 1
        
        return countProvince
    
    def isEdgeCity(self, i, j, isConnected: list[list[int]]) -> bool:
        
        if isConnected[i][j] == 1:
            return True
        
        return False


class TestFindCircleNum(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example1(self):
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        self.assertEqual(self.solver.findCircleNum(isConnected), 2)

    def test_example2(self):
        isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        self.assertEqual(self.solver.findCircleNum(isConnected), 3)

    def test_all_connected(self):
        isConnected = [[1,1,1],[1,1,1],[1,1,1]]
        self.assertEqual(self.solver.findCircleNum(isConnected), 1)

    def test_none_connected_except_self(self):
        isConnected = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        self.assertEqual(self.solver.findCircleNum(isConnected), 4)

    def test_two_components(self):
        isConnected = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
        self.assertEqual(self.solver.findCircleNum(isConnected), 2)

    def test_large_input(self):
        isConnected = [[1]*5 for _ in range(5)]  # All cities are connected
        self.assertEqual(self.solver.findCircleNum(isConnected), 1)


if __name__ == "__main__":
    unittest.main()