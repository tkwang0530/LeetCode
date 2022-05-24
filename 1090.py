"""
1090. Largest Values From Labels
There is a set of n items. You are given two integer arrays values and labels where the value and the label of the i-th element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

Choose a subset s of the n elements such that:
- The size of the subset s is less than or equal to numWanted.
- There are at most useLimit items with the same label in s.

The score of a subset is the sum of values in the subset.

Return the maximum score of a subset s.

Example1:
Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth items.

Example2:
Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third items.

Example3:
Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
Output: 16
Explanation: The subset chosen is the first and fourth items.

Constraints:
n == values.length == labels.length
1 <= n <= 2 * 10^4
0 <= values[i], labels[i] <= 2 * 10^4
1 <= numWanted, useLimit <= n
"""

"""
Note:
1. Greedy + HashTable: O(nlogn) time | O(n) space - where n is the length of array values
"""

import collections
from typing import List
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        labelCount = collections.defaultdict(int)
        valueLabels = [(value, label) for value, label in zip(values, labels)]
        valueLabels.sort(reverse=True)

        i = total = chosenCount = 0
        while i < len(valueLabels) and chosenCount < numWanted:
            value, label = valueLabels[i]
            if labelCount[label] == useLimit:
                i += 1
                continue
            chosenCount += 1
            total += value
            labelCount[label] += 1
            i += 1
        return total


# Unit Tests
import unittest
funcs = [Solution().largestValsFromLabels]
class TestLargestValsFromLabels(unittest.TestCase):
    def testLargestValsFromLabels1(self):
        for func in funcs:
            values = [5,4,3,2,1]
            labels = [1,1,2,2,3]
            numWanted = 3
            useLimit = 1
            self.assertEqual(func(values=values, labels=labels, numWanted=numWanted, useLimit=useLimit), 9)

    def testLargestValsFromLabels2(self):
        for func in funcs:
            values = [5,4,3,2,1]
            labels = [1,3,3,3,2]
            numWanted = 3
            useLimit = 2
            self.assertEqual(func(values=values, labels=labels, numWanted=numWanted, useLimit=useLimit), 12)

    def testLargestValsFromLabels3(self):
        for func in funcs:
            values = [9,8,8,7,6]
            labels = [0,0,0,1,1]
            numWanted = 3
            useLimit = 1
            self.assertEqual(func(values=values, labels=labels, numWanted=numWanted, useLimit=useLimit), 16)


if __name__ == "__main__":
    unittest.main()
