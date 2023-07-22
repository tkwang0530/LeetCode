"""
1893. Check if All the Integers in a Range Are Covered
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

Example1:
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.

Example2:
Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.

Constraints:
1 <= ranges.length <= 50
1 <= start_i <= end_i <= 50
1 <= left <= right <= 50
"""

"""
Note:
1. Sweep Line + HashTable: O(r) time | O(r) space - where r is the length of array ranges
"""

import collections
from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sweep = collections.defaultdict(int)
        for start, end in ranges:
            sweep[start] += 1
            sweep[end + 1] -= 1
        
    
        times = sorted(sweep.keys())
        if len(times) == 0 or times[0] > left or times[-1] < right:
            return False
        
        current = 0
        for t in times:
            current += sweep[t]
            if current < 1 and left <= t <= right:
                return False
        return True


# Unit Tests
import unittest
funcs = [Solution().isCovered]

class TestIsCovered(unittest.TestCase):
    def testIsCovered1(self):
        for func in funcs:
            ranges = [[1,2],[3,4],[5,6]]
            left = 2
            right = 5
            self.assertEqual(func(ranges=ranges, left=left, right=right), True)

    def testIsCovered2(self):
        for func in funcs:
            ranges = [[1,10],[10,20]]
            left = 21
            right = 21
            self.assertEqual(func(ranges=ranges, left=left, right=right), False)

if __name__ == "__main__":
    unittest.main()