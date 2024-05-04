"""
881. Boats to Save People
description: https://leetcode.com/problems/boats-to-save-people/description/
"""

"""
Note:
1. SortedList: O(nlogn) time | O(n) space - where n is the length of people
2. Two Pointers: O(nlogn) time | O(1) space - where n is the length of people
"""

from typing import List
import unittest
from sortedcontainers import SortedList
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        bst = SortedList()
        for i, weight in enumerate(people):
            bst.add((weight, i))
        
        while bst:
            weight, _ = bst.pop()

            # find partner
            if limit-weight > 0 and bst:
                idx = bst.bisect_left((limit-weight, -1))
                if idx == len(bst):
                    bst.pop()
                elif idx < len(bst) and bst[idx][0] == limit-weight:
                    bst.pop(idx)
                elif idx-1 >= 0:
                    bst.pop(idx-1)
            
            boats += 1
        return boats

class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        boats = 0
        while left <= right:
            if people[left]+people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            boats += 1
        return boats
# Unit Tests
funcs = [Solution().numRescueBoats, Solution2().numRescueBoats]


class TestNumRescueBoats(unittest.TestCase):
    def testNumRescueBoats1(self):
        for func in funcs:
            people = [1,2]
            limit = 3
            self.assertEqual(func(people=people, limit=limit), 1)

    def testNumRescueBoats2(self):
        for func in funcs:
            people = [3,2,2,1]
            limit = 3
            self.assertEqual(func(people=people, limit=limit), 3)

    def testNumRescueBoats3(self):
        for func in funcs:
            people = [3,5,3,4]
            limit = 5
            self.assertEqual(func(people=people, limit=limit), 4)


if __name__ == "__main__":
    unittest.main()
