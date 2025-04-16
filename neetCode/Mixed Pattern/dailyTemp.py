import unittest

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """returns the number of days you have to wait for a temparature of
        an upcoming day to be higher than current day"""
        
        def discApproach():
            """
            value of temp will be between 30 - 100 inclusive
            No need to worry about an empty input array (temperature)
            
            Bruteforce approach I would take will be O(n^2) time complexity, utilizing
            linear search through input array and tracking number of days till
            I hit a value higher than current day value and append that to 
            result array in it's respective index...
            
            Because len(temperatur == 10^5) I am concerned about TLE...Let me see 
            if I can think of an alternative and apply it within my alloted time. 
            
            If I cant think of another approach, I will use the bruteforce method 
            as proof of concept...
            
            Ok took me 45 minutes (not ideal) but I can use an altered monotonic 
            decreasing stack to solve the problem. It will allow for O(n) time 
            complexity but as a result of using O(n) space complexity
            """
            
            pass
            
        monoStack = []
        daysWaited = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            
            while monoStack and temperatures[i] > temperatures[monoStack[-1]]:
                daysWaited[monoStack[-1]] = i - monoStack[-1]
                monoStack.pop()
            
            monoStack.append(i)
        
        return daysWaited


class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        temperatures = [73,74,75,71,69,72,76,73]
        expected = [1,1,4,2,1,1,0,0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_example_2(self):
        temperatures = [30,40,50,60]
        expected = [1,1,1,0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_example_3(self):
        temperatures = [30,60,90]
        expected = [1,1,0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_all_decreasing(self):
        temperatures = [100, 90, 80, 70]
        expected = [0,0,0,0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_all_increasing(self):
        temperatures = [70, 71, 72, 73]
        expected = [1,1,1,0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_all_same(self):
        temperatures = [50, 50, 50, 50]
        expected = [0,0,0,0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_single_day(self):
        temperatures = [50]
        expected = [0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_two_days_no_warmer(self):
        temperatures = [55, 54]
        expected = [0, 0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

    def test_two_days_with_warmer(self):
        temperatures = [54, 55]
        expected = [1, 0]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), expected)

if __name__ == '__main__':
    unittest.main()