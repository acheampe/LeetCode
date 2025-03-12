import unittest
from typing import List

def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Return boolean, True if no overlap for meeting
    
    Time Complexity: O(n log n) 
    Space Complexity: O(1) 
    """

    # sort meeting time
    intervals.sort(key = lambda x : x[0])

    for i in range(len(intervals) - 1):
        nextStart = intervals[i + 1][0]
        prevEnd = intervals[i][1]
        if nextStart < prevEnd:
            return False

    return True

class TestMeetingRooms(unittest.TestCase):
    def test_non_overlapping(self):
        intervals = [[0, 30], [35, 50], [60, 90]]
        self.assertTrue(can_attend_meetings(intervals))

    def test_overlapping(self):
        intervals = [[0, 30], [25, 50], [60, 90]]
        self.assertFalse(can_attend_meetings(intervals))

    def test_adjacent_meetings(self):
        intervals = [[0, 10], [10, 20], [20, 30]]
        self.assertTrue(can_attend_meetings(intervals))

    def test_single_meeting(self):
        intervals = [[5, 10]]
        self.assertTrue(can_attend_meetings(intervals))

    def test_empty_intervals(self):
        intervals = []
        self.assertTrue(can_attend_meetings(intervals))

if __name__ == "__main__":
    unittest.main()
