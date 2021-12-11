"""
1055. Shortest Way to Form String
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e. "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1

Example1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of souce "abc"

Example2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

Constraints:
1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.
"""

""" 
1. Binary Search and compare index: O(nlogn) time | O(n) space
"""



import bisect, collections
class Solution(object):
    def shortestWay(self, source: str, target: str) -> int:
        stringIndices = collections.defaultdict(list)
        for i in range(len(source)):
            stringIndices[source[i]].append(i)
        
        ways = 1
        i = 0
        currentSourceIndex = -1
        while i < len(target):
            targetChar = target[i]
            if targetChar not in stringIndices:
                return -1

            # find the index to insert (currentSourceIndex) in stringIndices[targetChar] list
            index = bisect.bisect_right(stringIndices[targetChar], currentSourceIndex)

            if index >= len(stringIndices[targetChar]):
                currentSourceIndex = stringIndices[targetChar][0]
                ways += 1
            else:
                currentSourceIndex = stringIndices[targetChar][index]
            i += 1
        return ways



# Unit Tests
import unittest
funcs = [Solution().shortestWay]


class TestShortestWay(unittest.TestCase):
    def testShortestWay1(self):
        for func in funcs:
            source = "abc"
            target = "abcbc"
            self.assertEqual(func(source=source, target=target), 2)

    def testShortestWay2(self):
        for func in funcs:
            source = "abc"
            target = "acdbc"
            self.assertEqual(func(source=source, target=target), -1)

    def testShortestWay3(self):
        for func in funcs:
            source = "xyz"
            target = "xzyxz"
            self.assertEqual(func(source=source, target=target), 3)

if __name__ == "__main__":
    unittest.main()
