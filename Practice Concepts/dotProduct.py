import unittest
from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Initialize the Sparse Vector.
        Stores only nonzero values in a dictionary for efficiency.
        """
        self.values = {index: value for index, value in enumerate(nums) if value != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Compute the dot product between this sparse vector and another.
        TC: Worst case: O(n)
        SC: Worst case: O(n)
        """
        sumOutcome = 0

        for index, value in self.values.items():
            if index in vec.values:  # Only multiply if the index exists in both vectors
                sumOutcome += (vec.values[index] * value)
        
        return sumOutcome


class TestSparseVector(unittest.TestCase):
    def setUp(self):
        """Set up sparse vectors for testing"""
        self.v1 = SparseVector([1, 0, 0, 2, 3])
        self.v2 = SparseVector([0, 3, 0, 4, 0])
        self.v3 = SparseVector([0, 1, 0, 0, 0])
        self.v4 = SparseVector([0, 0, 0, 0, 2])
        self.v5 = SparseVector([0, 0, 0, 0, 0])
        self.v6 = SparseVector([2, 5, 0, 0, 1])

    def test_case1(self):
        """Test case from the problem statement"""
        self.assertEqual(self.v1.dotProduct(self.v2), 8)

    def test_case2(self):
        """Test case from the problem statement with zero result"""
        self.assertEqual(self.v3.dotProduct(self.v4), 0)

    def test_case3(self):
        """Edge case where both vectors are zero"""
        self.assertEqual(self.v5.dotProduct(self.v5), 0)

    def test_case4(self):
        """Edge case with one sparse and one dense"""
        self.assertEqual(self.v6.dotProduct(self.v1), 5)

    def test_case5(self):
        """Edge case with a mix of numbers"""
        self.assertEqual(self.v2.dotProduct(self.v6), 15)

if __name__ == "__main__":
    unittest.main()