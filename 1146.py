"""
1146. Snapshot Array
description: https://leetcode.com/problems/snapshot-array/description/
"""

"""
Note:
1. Binary Search
Total Space: O(S) - where S is the total number of set operations
__init__: O(length) time | O(length) space
set: O(1) time | O(1) space
snap: O(1) time | O(1) space
get: O(log(S)) time | O(1) space
"""

import unittest, bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.arrayHistory = [[[0,0]] for _ in range(length)]
        self.currentSnapID = 0

    def set(self, index: int, val: int) -> None:
        snapVal = self.arrayHistory[index][-1]
        if snapVal[0] == self.currentSnapID:
            snapVal[1] = val
        else:
            self.arrayHistory[index].append([self.currentSnapID, val])
            

    def snap(self) -> int:
        self.currentSnapID += 1
        return self.currentSnapID - 1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.arrayHistory[index], [snap_id, float("inf")])
        return self.arrayHistory[index][i-1][1]

# Unit Tests
classes = [SnapshotArray]

class TestSnapshotArray(unittest.TestCase):
    def testSnapshotArray1(self):
        for myclass in classes:
            snapshotArr = SnapshotArray(3)
            snapshotArr.set(0,5)
            snapshotArr.snap()
            snapshotArr.set(0,6)
            self.assertEqual(snapshotArr.get(0,0), 5)

if __name__ == "__main__":
    unittest.main()
