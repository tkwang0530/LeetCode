"""
401. Binary Watch
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
- For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.
- For example, "01:00" is not valid. It should be "1:00".

The minute must be consist of two digits and may contain a leading zero.
- For example, "10:2" is not valid. It should be "10:02".

Example1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example2:
Input: turnedOn = 9
Output: []

Constraints:
0 <= turnedOn <= 10
"""

"""
Note:
1. 
"""
from typing import List
import collections
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        onHours = collections.defaultdict(list)  
        onMinutes = collections.defaultdict(list)
        
        for minute in range(60):
            on = sum([int(char) for char in bin(minute)[2:]])
            minStr = str(minute) if len(str(minute)) == 2 else "0" + str(minute)
            onMinutes[on].append(minStr)
            
        for hour in range(12):
            on = sum([int(char) for char in bin(hour)[2:]])
            hourStr = str(hour)
            onHours[on].append(hourStr)
        
        output = []
        for onForHour in range(min(turnedOn, 3) + 1):
            onForMinute = turnedOn - onForHour
            for h in onHours[onForHour]:
                for m in onMinutes[onForMinute]:
                    output.append(h+":"+m)
        return output

# Unit Tests
import unittest
funcs = [Solution().readBinaryWatch]

class TestReadBinaryWatch(unittest.TestCase):
    def testReadBinaryWatch1(self):
        for func in funcs:
            turnedOn = 1
            self.assertEqual(sorted(func(turnedOn=turnedOn)), sorted(["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]))

    def testReadBinaryWatch2(self):
        for func in funcs:
            turnedOn = 9
            self.assertEqual(sorted(func(turnedOn=turnedOn)), sorted([]))

if __name__ == "__main__":
    unittest.main()