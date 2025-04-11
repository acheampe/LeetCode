import unittest

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """return 1-index pointers for the of the values 
        that will sum to target"""
        
        def approachAndQuestion():
            """will there be any negative vals? - though if negative it won't matter 
            since there is a nondecreasing order.
            Base on constraints it looks like I do not need to worry about input
            length less than 2 nor do i need to worry about empty inputs
            
            Since input is in non-decreasing sorted order, I believe this can be 
            executed O(n) and O(1) TC and SC respectively using a two pointer
            """
            pass
        
        leftPointer, rightPointer = 0, len(numbers) - 1
        
        while leftPointer < rightPointer:
            
            if numbers[leftPointer] + numbers[rightPointer] == target: 
                return [leftPointer + 1, rightPointer + 1]
        
            elif numbers[leftPointer] + numbers[rightPointer] > target: 
                rightPointer -= 1
            
            else:
                leftPointer += 1
        
        return [-1, -1] # no solution but this should not be reached
                

class TestTwoSumII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.sol.twoSum(numbers, target), [1, 2])

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(self.sol.twoSum(numbers, target), [1, 3])

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        self.assertEqual(self.sol.twoSum(numbers, target), [1, 2])

    def test_with_duplicates(self):
        numbers = [1, 1, 2, 3]
        target = 2
        self.assertEqual(self.sol.twoSum(numbers, target), [1, 2])

    def test_large_input(self):
        numbers = list(range(1, 10001))
        target = 19999
        self.assertEqual(self.sol.twoSum(numbers, target), [9999, 10000])

    def test_negative_numbers(self):
        numbers = [-1000, -500, 0, 200, 600]
        target = 100
        self.assertEqual(self.sol.twoSum(numbers, target), [2, 5])

if __name__ == '__main__':
    unittest.main()
