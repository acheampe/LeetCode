import unittest

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        def discussApproach():
            """I am going to attempt initializing arr of target length with an empty
            array initialized in each position then append speed in respective position
            
            During iteration if speed catches up to a slower value, we append that, by the time we reach target
            this will give me the different groups of fleets that reached target at the same time...
            I do need to be careful with a car that reaches target at the same time as a fleet and add it to the fleet. 
            """
        
        # defensive code 
        assert len(position) == len(speed), "length of position arr must match length of speed arr"
        
        highway = [[]] * (target + 1)
        
        # position vehicles
        for i in range(len(position)):
            highway[position[i]] = (speed[i])
        
        print(highway)
                

class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        self.assertEqual(self.sol.carFleet(target, position, speed), 3)

    # def test_example2(self):
    #     target = 10
    #     position = [3]
    #     speed = [3]
    #     self.assertEqual(self.sol.carFleet(target, position, speed), 1)

    # def test_example3(self):
    #     target = 100
    #     position = [0, 2, 4]
    #     speed = [4, 2, 1]
    #     self.assertEqual(self.sol.carFleet(target, position, speed), 1)

    # def test_all_same_speed(self):
    #     target = 100
    #     position = [10, 20, 30]
    #     speed = [1, 1, 1]
    #     self.assertEqual(self.sol.carFleet(target, position, speed), 3)

    # def test_one_catches_others(self):
    #     target = 10
    #     position = [0, 2, 4]
    #     speed = [3, 2, 1]
    #     self.assertEqual(self.sol.carFleet(target, position, speed), 1)

    # def test_reverse_order(self):
    #     target = 10
    #     position = [8, 5, 2]
    #     speed = [1, 2, 3]
    #     self.assertEqual(self.sol.carFleet(target, position, speed), 1)

    # def test_edge_case_large_values(self):
    #     target = 10**6
    #     position = [0, 1, 2]
    #     speed = [1, 2, 3]
    #     self.assertEqual(self.sol.carFleet(target, position, speed), 1)

if __name__ == '__main__':
    unittest.main()