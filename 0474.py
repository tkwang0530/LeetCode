"""
474. Ones and Zeroes
You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Example1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

Constraints:
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs consists only of digits '0' and '1'.
1 <= m, n <= 100
"""

""" 
1. dfs (bottom up): O(n) time | O(n) space - where n is the number of all possible subsets
2. dp: O(n) time | O(n) space - where n is the number of all possible subsets
"""

import collections
from typing import List, Tuple, Set
class Solution(object):
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        container = [0] # [maxLength]
        def dfs(index) -> Set[Tuple[int, int, int]]:
            if index >= len(strs):
                return set([(0, 0, 0)]) # numOfZero, numOfOne, len

            numCounts = collections.Counter(strs[index])
            currentSet = dfs(index+1)
            for numOfZero, numOfOne, length in currentSet.copy():
                zeroes, ones = numOfZero+numCounts['0'], numOfOne+numCounts['1']
                if zeroes <= m and ones <= n:
                    currentSet.add((zeroes, ones, length+1))
                    container[0] = max(container[0], length+1)
            return currentSet
        dfs(0)
        return container[0]

    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        maxLength = 0
        preSet = set([(0, 0, 0)]) # numOfZero, numOfOne, len
        preSeq = [(0, 0, 0)]
        for index in range(len(strs) - 1, -1, -1):
            numCounts = collections.Counter(strs[index])
            for i in range(len(preSet)):
                preZeroes, preOnes, preLength = preSeq[i]
                zeroes, ones, length = preZeroes+numCounts['0'], preOnes+numCounts['1'], preLength+1
                if zeroes <= m and ones <= n and (zeroes, ones, length) not in preSet:
                    preSet.add((zeroes, ones, length))
                    preSeq.append((zeroes, ones, length))
                    maxLength = max(maxLength, length)
        return maxLength
                    

# Unit Tests
import unittest
funcs = [Solution().findMaxForm, Solution().findMaxForm2]


class TestFindMaxForm(unittest.TestCase):
    def testFindMaxForm1(self):
        for func in funcs:
            strs = ["10","0001","111001","1","0"]
            m = 5
            n = 3
            self.assertEqual(func(strs=strs, m=m, n=n), 4)

    def testFindMaxForm2(self):
        for func in funcs:
            strs = ["10","0","1"]
            m = 1
            n = 1
            self.assertEqual(func(strs=strs, m=m, n=n), 2)

if __name__ == "__main__":
    unittest.main()
