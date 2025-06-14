import unittest

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Sort by position descending
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        
        fleetCount = 0
        lastTime = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > lastTime:
                fleetCount += 1
                lastTime = time

        return fleetCount
# class Solution:
#     def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
#         def discussApproach():
#             """I am going to attempt initializing arr of target length with an empty
#             array initialized in each position then append speed in respective position
            
#             During iteration if speed catches up to a slower value, we append that, by the time we reach target
#             this will give me the different groups of fleets that reached target at the same time...
#             I do need to be careful with a car that reaches target at the same time as a fleet and add it to the fleet. 
            
#             Ignore previous pattern...a better approach will be to iterate backwards and calculate for speed and add speed to a set.
#             The set will allow us to count fleets because they would all get there at the same time.
#             """
        
#         # defensive code 
#         assert len(position) == len(speed), "length of position arr must match length of speed arr"
#         pairArr = list(zip(position, speed))
        
#         # sort by position
#         pairArr.sort(key=lambda x: -x[0])
#         pairsWithTime = []
                
#         # add time
#         for pair in pairArr:
#             pos, spd = pair
#             #calc for time to finish line
#             dist = target - pos
#             time = (dist/spd)
#             pairsWithTime.append((pos, spd, time))
        
#         # Count fleet
#         fleetCount = 0
#         lastTime = 0

#         for _, _, time in pairsWithTime:
#             if time > lastTime:
#                 fleetCount += 1
#                 lastTime = time

#         return fleetCount

class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        self.assertEqual(self.sol.carFleet(target, position, speed), 3)

    def test_example2(self):
        target = 10
        position = [3]
        speed = [3]
        self.assertEqual(self.sol.carFleet(target, position, speed), 1)

    def test_example3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        self.assertEqual(self.sol.carFleet(target, position, speed), 1)

    def test_all_same_speed(self):
        target = 100
        position = [10, 20, 30]
        speed = [1, 1, 1]
        self.assertEqual(self.sol.carFleet(target, position, speed), 3)

    def test_one_catches_others(self):
        target = 10
        position = [0, 2, 4]
        speed = [3, 2, 1]
        self.assertEqual(self.sol.carFleet(target, position, speed), 1)

    def test_reverse_order(self):
        target = 10
        position = [8, 5, 2]
        speed = [1, 2, 3]
        self.assertEqual(self.sol.carFleet(target, position, speed), 3)

    def test_edge_case_large_values(self):
        target = 10**6
        position = [0, 1, 2]
        speed = [1, 2, 3]
        self.assertEqual(self.sol.carFleet(target, position, speed), 3)

if __name__ == '__main__':
    unittest.main()