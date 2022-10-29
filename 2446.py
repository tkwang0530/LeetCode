"""
2446. Determine if Two Events Have Conflict
You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:
- event1 = [startTime1, endTime1] and
- event2 = [startTime2, endTime2].

Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.

Example1:
Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.

Example2:
Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.

Example3:
Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.

Constraints:
event1.length == event2.length == 2.
event1[i].length == event2[i].length == 5
startTime1 <= endTime1
startTime2 <= endTime2
All the event times follow the HH:MM format.
"""

"""
Note:
1. String: O(1) time | O(1) space
"""




import unittest
from typing import List
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])


# Unit Tests
funcs = [Solution().haveConflict]


class TestHaveConflict(unittest.TestCase):
    def testHaveConflict1(self):
        for func in funcs:
            event1 = ["01:15", "02:00"]
            event2 = ["02:00", "03:00"]
            self.assertEqual(func(event1=event1, event2=event2), True)

    def testHaveConflict2(self):
        for func in funcs:
            event1 = ["01:00", "02:00"]
            event2 = ["01:20", "03:00"]
            self.assertEqual(func(event1=event1, event2=event2), True)

    def testHaveConflict3(self):
        for func in funcs:
            event1 = ["10:00", "11:00"]
            event2 = ["14:00", "15:00"]
            self.assertEqual(func(event1=event1, event2=event2), False)


if __name__ == "__main__":
    unittest.main()
