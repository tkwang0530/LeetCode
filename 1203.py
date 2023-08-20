"""
1203. Sort Items by Groups Respecting Dependencies
description: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
"""

"""
Note:
1. topological sort: O(n^2) time | O(mn+n^2) space
"""

from typing import List
import collections
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        beforeItemSet = collections.defaultdict(set)
        afterItemSet = collections.defaultdict(set)

        unlockItemsMap = collections.defaultdict(list)
        otherGroupDepCount = collections.defaultdict(int)
        for i,items in enumerate(beforeItems):
            if len(items) == 0:
                unlockItemsMap[group[i]].append(i)
            else:
                beforeItemSet[i] = set(items)
                for item in items:
                    if group[item] != group[i]:
                        otherGroupDepCount[group[i]] += 1
                    afterItemSet[item].add(i)

        output = []
        readyGroups = []

        for g in range(m):
            if otherGroupDepCount[g] == 0:
                readyGroups.append(g)

        def processGroup(groupTurnNumber) -> int:
            while unlockItemsMap[groupTurnNumber]:
                item = unlockItemsMap[groupTurnNumber].pop()
                output.append(item)
                for afterItem in afterItemSet[item]:
                    if group[afterItem] != group[item]:
                        otherGroupDepCount[group[afterItem]] -= 1
                        if otherGroupDepCount[group[afterItem]] == 0:
                            readyGroups.append(group[afterItem])
                    beforeItemSet[afterItem].remove(item)
                    if not beforeItemSet[afterItem]:
                        unlockItemsMap[group[afterItem]].append(afterItem)
        
        while len(output) < n:
            processGroup(-1)
            if not readyGroups:
                return []
            else:
                processGroup(readyGroups.pop())
        
        return output

# Unit Tests
import unittest
funcs = [Solution().sortItems]
class TestSortItems(unittest.TestCase):
    def testSortItems1(self):
        for sortItems in funcs:
            n = 8
            m = 2
            group = [-1,-1,1,0,0,1,0,-1]
            beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
            self.assertEqual(sortItems(n=n, m=m, group=group, beforeItems=beforeItems), [7,0,5,2,6,3,4,1])

    def testSortItems2(self):
        for sortItems in funcs:
            n = 8
            m = 2
            group = [-1,-1,1,0,0,1,0,-1]
            beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
            self.assertEqual(sortItems(n=n, m=m, group=group, beforeItems=beforeItems), [])

if __name__ == "__main__":
    unittest.main()
