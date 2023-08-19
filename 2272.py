"""
2272. Substring With Largest Variance
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

Example1:
Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

Example2:
Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""

"""
Note:
1. PrefixCounter: O(n^2) time | O(26n) space - where n is the length of string s
2. Weird Kadane: O(n) time | O(1) space
For each pair of characters (c1, c2), find their maximum of count(c1) - count(c2) in the substrings.
ref: https://leetcode.com/problems/substring-with-largest-variance/solutions/2039178/weird-kadane/
"""

class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        preCounter = [[0] * 26 for _ in range(n+1)]
        for i in range(1, n+1):
            preCounter[i] = preCounter[i-1].copy()

            charIdx = ord(s[i-1]) - ord("a")
            preCounter[i][charIdx] += 1
        
        # return the variance of substring start from i (including) end to j (excluding)
        def query(i: int, j: int) -> int:
            counter = [0] * 26

            smallest = float("inf")
            largest = float("-inf")
            for k in range(26):
                counter[k] = preCounter[j][k] - preCounter[i][k]
                if counter[k] > 0:
                    smallest = min(smallest, counter[k])
                    largest = max(largest, counter[k])
            return largest - smallest

        largestVariance = 0
        for i in range(n):
            for j in range(i+1, n+1):
                largestVariance = max(
                    largestVariance,
                    query(i, j)
                )
        return largestVariance

class Solution2:
    def largestVariance(self, s: str) -> int:
        uniqueChars = set(s)
        res = 0
        for a in uniqueChars:
            for b in uniqueChars:
                variance = 0
                hasB = False
                firstB = False
                for char in s:
                    variance += char == a
                    if char == b:
                        hasB = True
                        if firstB and variance >= 0:
                            firstB = False
                        else:
                            variance -= 1
                            if variance < 0:
                                firstB = True
                                variance = -1
                    res = max(res, variance if hasB else 0)
        return res

# Unit Tests
import unittest
funcs = [Solution().largestVariance, Solution2().largestVariance]
class TestLargestVariance(unittest.TestCase):
    def testLargestVariance1(self):
        for largestVariance in funcs:
            s = "aababbb"
            self.assertEqual(largestVariance(s=s), 3)

    def testLargestVariance2(self):
        for largestVariance in funcs:
            s = "abcde"
            self.assertEqual(largestVariance(s=s), 0)

if __name__ == "__main__":
    unittest.main()
