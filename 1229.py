"""
1229. Meeting Scheduler
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration 'duration', return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []

Constraints:
1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6
"""

"""
Notes:
1. Two Pointers: O(nlogn+mlogm) time | O(n+m) space
2. Line Sweep: O((n+m)log(n+m)) time | O(n+m) space
"""
import collections
from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        def intersect(slot1, slot2) -> List[int]:
            start, end = max(slot1[0], slot2[0]), min(slot1[1], slot2[1])
            return [start, end] if start < end else [0,0]

        idx1 = idx2 = 0
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        while idx1 < len(slots1) and idx2 < len(slots2):
            slot1 = slots1[idx1]
            slot2 = slots2[idx2]
            intersectSlot = intersect(slot1, slot2)
            if (intersectSlot[1]-intersectSlot[0]) >= duration:
                return [intersectSlot[0], intersectSlot[0]+duration]
            elif slot1[1] < slot2[1]:
                idx1 += 1
            else:
                idx2 += 1
        return []
    
    def minAvailableDuration2(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        timeIncreasePeople = collections.defaultdict(int)
        for start, end in slots1+slots2:
            timeIncreasePeople[start] += 1
            timeIncreasePeople[end] -= 1
        
        peopleCount = 0
        validStart = -1
        for time in sorted(timeIncreasePeople.keys()):
            peopleCount += timeIncreasePeople[time]
            
            if validStart != -1 and time - validStart >= duration:
                return [validStart, validStart+duration]
            
            if peopleCount < 2:
                validStart = -1
            else:
                validStart = time
        return []


# Unit Tests
import unittest
funcs = [Solution().minAvailableDuration, Solution().minAvailableDuration2]

class TestMinAvailableDuration(unittest.TestCase):
    def testMinAvailableDuration1(self):
        for func in funcs:
            slots1 = [[10,50],[60,120],[140,210]]
            slots2 = [[0,15],[60,70]]
            duration = 8
            self.assertEqual(func(slots1=slots1, slots2=slots2, duration=duration), [60,68])

    def testMinAvailableDuration2(self):
        for func in funcs:
            slots1 = [[10,50],[60,120],[140,210]]
            slots2 = [[0,15],[60,70]]
            duration = 12
            self.assertEqual(func(slots1=slots1, slots2=slots2, duration=duration), [])

    def testMinAvailableDuration3(self):
        for func in funcs:
            slots1 = [[10,60]]
            slots2 = [[12,17],[21,50]]
            duration = 8
            self.assertEqual(func(slots1=slots1, slots2=slots2, duration=duration), [21, 29])

    def testMinAvailableDuration4(self):
        for func in funcs:
            slots1 = [[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]
            slots2 = [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
            duration = 456085
            self.assertEqual(func(slots1=slots1, slots2=slots2, duration=duration), [98730764,99186849])

        

456085
if __name__ == "__main__":
    unittest.main()