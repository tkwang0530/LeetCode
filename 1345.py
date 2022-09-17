"""
1345. Jump Game IV
Given an array of integers arr, you are initially positioned at the first index of the array.
In one step you can jump from index i to index:
- i + 1 where i + 1 < arr.length.
- i - 1 where i - 1 >= 0.
- j where arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.
Notice that you can not jump outside of the array at any time.

Example1:
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example2:
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.

Example3:
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
"""

"""
Note:
1. BFS: O(n) time | O(n) space - where n is the length of arr
"""




import unittest
import collections
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        portalIndice = collections.defaultdict(list)
        for i, val in enumerate(arr):
            portalIndice[val].append(i)

        n = len(arr)
        queue = collections.deque([(0, 0)])  # idx, step

        markers = [0] * len(arr)  # 0: unknown, 1: visited
        markers[0] = 1
        while queue:
            idx, step = queue.popleft()
            val = arr[idx]

            if idx == n-1:
                return step

            for nextIdx in portalIndice[val] + [idx-1, idx+1]:
                if not (0 <= nextIdx < n) or markers[nextIdx]:
                    continue
                queue.append((nextIdx, step+1))
                markers[nextIdx] = 1
            portalIndice[val] = []

        return -1


# Unit Tests
funcs = [Solution().minJumps]


class TestMinJumps(unittest.TestCase):
    def testMinJumps1(self):
        for func in funcs:
            arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
            self.assertEqual(func(arr=arr), 3)

    def testMinJumps2(self):
        for func in funcs:
            arr = [7]
            self.assertEqual(func(arr=arr), 0)

    def testMinJumps3(self):
        for func in funcs:
            arr = [7, 6, 9, 6, 9, 6, 9, 7]
            self.assertEqual(func(arr=arr), 1)


if __name__ == "__main__":
    unittest.main()
