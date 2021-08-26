"""
1051. Height Checker
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i]

Example1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Example2:
Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

Example3:
Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100
"""

"""
Note:
1. Sort + One Pass: O(nlogn) time | O(n) space
2. Counting Sort: O(n) time | O(n) space
"""

import unittest
from  typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        return count

    def heightChecker2(self, heights: List[int]) -> int:
        heightFreq = {}
        for height in heights:
            heightFreq[height] = heightFreq.get(height, 0) + 1
        
        currHeight = count = 0
        for i in range(len(heights)):
            while heightFreq.get(currHeight, 0) == 0:
                currHeight += 1
            if currHeight != heights[i]:
                count += 1
            heightFreq[currHeight] -= 1
        return count


# Unit Tests
funcs = [Solution().heightChecker, Solution().heightChecker2]


class TestHeightChecker(unittest.TestCase):
    def testHeightChecker1(self):
        for func in funcs:
            heights = [1,1,4,2,1,3]
            self.assertEqual(func(heights=heights), 3)

    def testHeightChecker2(self):
        for func in funcs:
            heights = [5,1,2,3,4]
            self.assertEqual(func(heights=heights), 5)

    def testHeightChecker3(self):
        for func in funcs:
            heights = [1,2,3,4,5]
            self.assertEqual(func(heights=heights), 0)


if __name__ == "__main__":
    unittest.main()
