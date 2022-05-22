"""
1488. Avoid Flood in the City
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the n-th lake, the n-th lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:
- rains[i] > 0 means there will be rains over the rains[i] lake.
- rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.

Return an array ans where:
- ans.length == rains.length
- ans[i] == -1 if rains[i] > 0.
- ans[i] is the lake you choose to dry in the i-th day if rains[i] == 0.

If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you choose to dry a full lake, it becomes empty, but if you choose to dry an empty lake, nothing changes.

Example1:
Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

Example2:
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

Example3:
Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

Constraints:
1 <= rains.length <= 10^5
0 <= rains[i] <= 10^9
"""

""" 
Notes:
1. HashTable + minHeap: O(nlogn) time | O(n) space
2. SortedList (BST): O(nlogn) time | O(n) space
"""

from sortedcontainers import SortedList
import collections, heapq
from typing import List
class Solution(object):
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        minHeap = []
        lakeRainDays = collections.defaultdict(list)
        full = set()

        for i in range(n-1, -1, -1):
            rainLake = rains[i]
            lakeRainDays[rainLake].append(i)

        for i, rainLake in enumerate(rains):
            if rainLake > 0:
                if rainLake in full:
                    return []
                full.add(rainLake)
                lakeRainDays[rainLake].pop()
                
                # only push rainLake's smallest rain day into minHeap if there is at least one rainning day on that lake
                if not lakeRainDays[rainLake]:
                    continue
                heapq.heappush(minHeap, lakeRainDays[rainLake][-1])
            elif not minHeap:
                ans[i] = 1
            else:
                closestRainDay = heapq.heappop(minHeap)
                full.remove(rains[closestRainDay])
                ans[i] = rains[closestRainDay]
        return ans

    def avoidFlood2(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        zeroIndices = SortedList()
        full = {}
        for i, rainLake in enumerate(rains):
            if rainLake > 0 and rainLake not in full:
                full[rainLake] = i
            elif rainLake > 0:
                lastRainDay = full[rainLake]
                idx = zeroIndices.bisect_right(lastRainDay)
                if idx == len(zeroIndices):
                    return []
                zeroDay = zeroIndices[idx]
                ans[zeroDay] = rainLake
                zeroIndices.remove(zeroDay)
                full[rainLake] = i
            else:
                zeroIndices.add(i)
                ans[i] = 1
        return ans

# Unit Tests
import unittest
funcs = [Solution().avoidFlood, Solution().avoidFlood2]

class TestAvoidFlood(unittest.TestCase):
    def testAvoidFlood1(self):
        for func in funcs:
            rains = [1,2,3,4]
            self.assertEqual(func(rains=rains), [-1,-1,-1,-1])

    def testAvoidFlood2(self):
        for func in funcs:
            rains = [1,2,0,0,2,1]
            self.assertEqual(func(rains=rains), [-1,-1,2,1,-1,-1])

    def testAvoidFlood3(self):
        for func in funcs:
            rains = [1,2,0,1,2]
            self.assertEqual(func(rains=rains), [])

if __name__ == "__main__":
    unittest.main()
