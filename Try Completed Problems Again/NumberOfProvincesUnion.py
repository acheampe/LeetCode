from typing import List
import unittest

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        return the number of provinces 

        Args: isConnected -> 2D array matrix (adjacent matrix) List with boolen
        to indicate connection to neighbors 

        Return: Int -> number of individual provinces
        """

        # Establih space needed to solve problem:
        n = len(isConnected)
        parentCity = [i for i in range(n)]

        def find(currentLead):
            """
            Utilize path compression to find province lead

            Arg: current Lead, if not head of province -> Int

            Return: Head of province -> Int
            """

            if parentCity[currentLead] != currentLead:
                parentCity[currentLead] = find(parentCity[currentLead])
   
            return parentCity[currentLead]
        
        def union(city1, city2):
            """
            Unify both connected cities by establishing province lead

            Arg: City1 and City2 --> Int

            Return: Updates parent relationship
            """
            # Find head of each city
            root1 = find(city1)
            root2 = find(city2)

            if root1 != root2:
                # Establish lead
                parentCity[root2] = root1
        
        for i in range(n):
            for j in range(i+1, n): # To reduce redundancy

                # Unite connected neighbors
                if isConnected[i][j] == 1:
                    union(i, j)
        
        # Find and add head of each province to a set
        province = set()
        for i in range(n):
            province.add(find(i))
        
        # return number of province
        return len(province)
        
    
    def approachSolution(self):
        """
        Approaching this problem using Union Find is an excellent way to 
        tackle problem with separation of concern approach. 

        A Find algorithm is establish to find the head of a connected city, this will allow us to accurately count it as one province.

        A Union algorithm will allow us to unite neighbors that are connected

        And then parsing through the isConnected will allow us to unite connected neighbors (through Union function)

        The last process is now to add head of all provinces to a set and return the length of that set which will return the int value of the number of province needed

        Space Complexity: O(n) due to established parent array
        Time Complexity: O(n)
        """

        pass


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