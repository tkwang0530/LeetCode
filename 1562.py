"""
1562. Find Latest Group of Size M
description: https://leetcode.com/problems/find-latest-group-of-size-m/description/
"""

"""
Note:
1. bst + counter: O(nlogn) time | O(n) space - where n is the length of array arr
2. Count the length of Groups: O(n) time | O(n) space - where n is the length of array arr
the length value is updated on the leftmost and the right most bit of the group
The length value inside the group may be outdated
ref: https://leetcode.com/problems/find-latest-group-of-size-m/solutions/806786/java-c-python-count-the-length-of-groups-o-n/
"""

from typing import List
from sortedcontainers import SortedList
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        bst = SortedList([(1,n)])
        sizeCounter = [0] * (n+1)
        sizeCounter[n] = 1

        def getSize(interval: List[int]) -> int:
            return interval[1] - interval[0] + 1

        def split(bst, idx):
            i = bst.bisect_left((idx, float("inf")))
            interval = bst[i-1]
            sizeCounter[getSize(interval)] -= 1
            bst.remove(interval)
            leftInterval = (interval[0], idx-1)
            rightInterval = (idx+1, interval[1])
            if getSize(leftInterval) > 0:
                sizeCounter[getSize(leftInterval)] += 1
                bst.add(leftInterval)
            if getSize(rightInterval) > 0:
                sizeCounter[getSize(rightInterval)] += 1
                bst.add(rightInterval)
            

        for i in range(n-1, -1, -1):
            if sizeCounter[m] > 0:
                return i+1
            
            split(bst, arr[i])
        return -1

class Solution2:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return m
        sizes = [0] * (n+2)
        candidate = -1
        for i, idx in enumerate(arr):
            sizeLeft, sizeRight = sizes[idx-1], sizes[idx+1]
            if m in (sizeLeft, sizeRight):
                candidate = i
            sizes[idx-sizeLeft] = sizes[idx+sizeRight] = sizeLeft+sizeRight+1
        return candidate

# Unit Tests
import unittest
funcs = [Solution().findLatestStep, Solution2().findLatestStep]
class TestFindLatestStep(unittest.TestCase):
    def testFindLatestStep1(self):
        for findLatestStep in funcs:
            arr = [3,5,1,2,4]
            m = 1
            self.assertEqual(findLatestStep(arr=arr, m=m), 4)

    def testFindLatestStep2(self):
        for findLatestStep in funcs:
            arr = [3,1,5,4,2]
            m = 2
            self.assertEqual(findLatestStep(arr=arr, m=m), -1)

if __name__ == "__main__":
    unittest.main()
