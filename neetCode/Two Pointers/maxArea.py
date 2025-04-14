import unittest

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """return the maxArea of water given heights"""
        
        def discussApproach():
            """
            Given that there will be at minimum height of length two, we
            do not need to worry about an empty edge case
            
            heights are garanteed to be between 0 and 10^4, no need to worry about
            negative integers
            
            I think a two pointer approach will be most appropriate to calc. this
            in O(n) TC and O(1) SC
            
            We could approach this using a nested loop on O(n^2) but that will not be
            ideal 
            """
            pass
        
        # heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        # Area = height * length
            
        leftIndex, rightIndex = 0, len(heights) - 1
        maxArea = float('-inf')
        
        while leftIndex < rightIndex:
            length = rightIndex - leftIndex
            height = min(heights[leftIndex], heights[rightIndex]) # To calc max height the water can be without flowing over
            
            maxArea = max(maxArea, (height * length))
            
            if heights[leftIndex] == heights[rightIndex]:
                
                if leftIndex + 1 < rightIndex and heights[leftIndex + 1] > heights[rightIndex - 1]:
                    leftIndex += 1
                
                else:
                    rightIndex -= 1
            
            elif heights[leftIndex] < heights[rightIndex]:
                leftIndex += 1
            
            else:
                rightIndex -= 1
                
        return int(maxArea)
        

class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(self.sol.maxArea(height), expected)

    def test_example_2(self):
        height = [1, 1]
        expected = 1
        self.assertEqual(self.sol.maxArea(height), expected)

    def test_increasing(self):
        height = [1, 2, 3, 4, 5]
        expected = 6  # between 1 and 5
        self.assertEqual(self.sol.maxArea(height), expected)

    def test_decreasing(self):
        height = [5, 4, 3, 2, 1]
        expected = 6  # between 0 and 4
        self.assertEqual(self.sol.maxArea(height), expected)

    def test_plateau(self):
        height = [3, 3, 3, 3]
        expected = 9
        self.assertEqual(self.sol.maxArea(height), expected)

    def test_single_peak(self):
        height = [1, 2, 4, 3]
        expected = 4
        self.assertEqual(self.sol.maxArea(height), expected)

    def test_wide_flat_bottom(self):
        height = [1, 3, 2, 5, 25, 24, 5]
        expected = 24
        self.assertEqual(self.sol.maxArea(height), expected)

if __name__ == '__main__':
    unittest.main()