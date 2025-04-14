import unittest

class Solution:
    def trap(self, height: list[int]) -> int:
        """return the max area of water that can be trapped
        TC: O(n)  SC: O(1)
        """
        
        maxTrap = 0
        maxLeft, maxRight = float('-inf'), float('-inf')
        
        leftPointer, rightPointer = 0, len(height) - 1
        
        while leftPointer < rightPointer:
            
            maxLeft = max(maxLeft, height[leftPointer])
            maxRight = max(maxRight, height[rightPointer])
            
            if maxLeft < maxRight:
                maxTrap += max((maxLeft - height[leftPointer]), 0)
                leftPointer += 1
            
            else:
                maxTrap += max((maxRight - height[rightPointer], 0))
                rightPointer -= 1
        
        return maxTrap
            
            


class TestTrappingRainWater(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        expected = 6
        self.assertEqual(self.sol.trap(height), expected)

    def test_example_2(self):
        height = [4,2,0,3,2,5]
        expected = 9
        self.assertEqual(self.sol.trap(height), expected)

    def test_flat_surface(self):
        height = [0,0,0,0]
        expected = 0
        self.assertEqual(self.sol.trap(height), expected)

    def test_no_trap(self):
        height = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.sol.trap(height), expected)

    def test_valley(self):
        height = [5,0,5]
        expected = 5
        self.assertEqual(self.sol.trap(height), expected)

    def test_multiple_valleys(self):
        height = [3,0,1,3,0,5]
        expected = 8
        self.assertEqual(self.sol.trap(height), expected)

    def test_single_column(self):
        height = [1]
        expected = 0
        self.assertEqual(self.sol.trap(height), expected)

    def test_two_columns(self):
        height = [1, 2]
        expected = 0
        self.assertEqual(self.sol.trap(height), expected)

    def test_large_plateau(self):
        height = [0,2,2,2,0,2]
        expected = 2
        self.assertEqual(self.sol.trap(height), expected)

if __name__ == '__main__':
    unittest.main()