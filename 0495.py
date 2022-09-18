"""
495. Teemo Attacking
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

Example1:
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example2:
Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

Constraints:
1 <= timeSeries.length <= 10^4
0 <= timeSeries[i], duration <= 10^7
timeSeries is sorted in non-decreasing order.
"""

"""
Note:
1. Brute-Force: O(n) time | O(1) space - where n is the length of array timeSeries
"""




from typing import List
import unittest
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        interval = [-1, -2]
        total = 0
        for time in timeSeries:
            if time <= interval[1]:
                interval[1] = time+duration-1
                continue

            total += interval[1] - interval[0] + 1
            interval = [time, time+duration-1]

        return total + interval[1] - interval[0] + 1


# Unit Tests
funcs = [Solution().findPoisonedDuration]


class TestFindPoisonedDuration(unittest.TestCase):
    def testFindPoisonedDuration1(self):
        for func in funcs:
            timeSeries = [1, 4]
            duration = 2
            self.assertEqual(func(timeSeries=timeSeries, duration=duration), 4)

    def testFindPoisonedDuration2(self):
        for func in funcs:
            timeSeries = [1, 2]
            duration = 2
            self.assertEqual(func(timeSeries=timeSeries, duration=duration), 3)


if __name__ == "__main__":
    unittest.main()
