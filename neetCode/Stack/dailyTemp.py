import unittest

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        monoDecStack = []
        results = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            
            while monoDecStack and temperatures[i] > temperatures[monoDecStack[-1]]:
                topStack = monoDecStack.pop()
                results[topStack] = i - topStack
            
            monoDecStack.append(i)
        
        return results

class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        temperatures = [73,74,75,71,69,72,76,73]
        expected = [1,1,4,2,1,1,0,0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_example2(self):
        temperatures = [30,40,50,60]
        expected = [1,1,1,0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_example3(self):
        temperatures = [30,60,90]
        expected = [1,1,0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_all_same(self):
        temperatures = [70,70,70,70]
        expected = [0,0,0,0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_strictly_decreasing(self):
        temperatures = [80,70,60,50]
        expected = [0,0,0,0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_empty(self):
        temperatures = []
        expected = []
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
