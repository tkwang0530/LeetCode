"""
370. Range Addition
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.

Example1:
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]

Example2:
Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]

Constraints:
1 <= length <= 10^5
0 <= updates.length <= 10^4
0 <= startIdx_i <= endIdx_i < length
-1000 <= Inc_i <= 1000
"""

"""
Note:
1. Sweep Line + HashTable: O(u+length) time | O(u) space - where u is the length of array updates
"""

import collections
from typing import List
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        sweep = collections.defaultdict(int)
        for start, end, inc in updates:
            sweep[start] += inc
            sweep[end+1] -= inc
        
        value = 0
        arr = [0] * length
        for i in range(length):
            value += sweep[i]
            arr[i] = value
        return arr


# Unit Tests
import unittest
funcs = [Solution().getModifiedArray]

class TestGetModifiedArray(unittest.TestCase):
    def testGetModifiedArray1(self):
        for func in funcs:
            length = 5
            updates = [[1,3,2],[2,4,3],[0,2,-2]]
            self.assertEqual(func(length=length, updates=updates), [-2,0,3,5,3])

    def testGetModifiedArray2(self):
        for func in funcs:
            length = 10
            updates = [[2,4,6],[5,6,8],[1,9,-4]]
            self.assertEqual(func(length=length, updates=updates), [0,-4,2,2,2,4,4,-4,-4,-4])

if __name__ == "__main__":
    unittest.main()