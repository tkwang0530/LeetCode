"""
218. The Skyline Problem
description: https://leetcode.com/problems/the-skyline-problem/description/
"""

"""
Note:
1. events and heap: O(nlogn) time | O(n) space - where n is the length of array buildings
2. bst + HashTable: O(nlogn) time | O(n) space - where n is the length of array buildings
"""

import collections
from sortedcontainers import SortedList
from typing import List
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # add start-building events
        events = [(L, -H, R) for L, R, H in buildings]

        # also add end-building events (acts as building with 0 height)
        events += list({(R, 0, 0) for _, R, _ in buildings})

        # and sort the events in left -> right order
        events.sort()

        result = [[0, 0]] # [x, height]

        live = [(0, float("inf"))] # [-height, ending position]
        for pos, negH, R in events:
            # 1. pop buildings that are already ended
            # 2. if it's the start-building event, make the building alive
            # 3. if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos:
                heapq.heappop(live)
            if negH:
                heapq.heappush(live, (negH, R))
            if result[-1][1] != -live[0][0]:
                result += [ [pos, -live[0][0]] ]
        return result[1:]


class Solution2:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        locSet = set()
        locEvents = collections.defaultdict(list) # <loc>: [diff]
        for leftLoc, rightLoc, height in buildings:
            locEvents[leftLoc].append(height)
            locEvents[rightLoc].append(-1*height)
            locSet.add(leftLoc)
            locSet.add(rightLoc)
        
        locations = sorted(list(locSet))

        bst = SortedList()
        maxHeight = 0
        output = []
        for loc in locations:
            for diff in locEvents[loc]:
                if diff > 0:
                    bst.add(diff)
                else:
                    bst.remove(-1*diff)
            
            newMaxHeight = bst[-1] if bst else 0
            if maxHeight != newMaxHeight:
                output.append([loc, newMaxHeight])
            maxHeight = newMaxHeight
        return output

# Unit Tests
import unittest
funcs = [Solution().getSkyline, Solution2().getSkyline]


class TestGetSkyline(unittest.TestCase):
    def testGetSkyline1(self):
        for func in funcs:
            buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
            self.assertEqual(func(buildings=buildings), [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])

    def testGetSkyline2(self):
        for func in funcs:
            buildings = [[0,2,3],[2,5,3]]
            self.assertEqual(func(buildings=buildings), [[0,3],[5,0]])

if __name__ == "__main__":
    unittest.main()