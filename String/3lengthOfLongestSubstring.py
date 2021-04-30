import unittest

""" Approach1: Naive brute force
O(n^2) substring, each substring takes O(n) to check with a hashtable/array
Time complexity: O(n^3) => O(n*128^2)
Space complexity: O(128)
"""

""" Approach2: Optimized brute force
For each starting index i, find the longest substring.
O(n)*O(n) = O(n^2)
Time complexity: O(n^2) => O(n*128)
Space complexity: O(128)
"""

""" Approach3: HashTable/Sliding Window
reference: https://www.youtube.com/watch?v=LupZFfCCbAU&ab_channel=HuaHua
Window (i, j) with unique characters
1. Use a hashtable to store the last indies of each characters
2. Keep track the valid starting point. When there is a match update the starting point to the current one
i = max(i, m[s[j]] + 1), len = j - i + 1
Time complexity: O(n)
Space complexity: O(128)
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lastSeen = {}
        longest = [0, 1]  # [startIdx, endIdx + 1]
        startIdx = 0
        for i, char in enumerate(s):
            endIdx = i
            if char in lastSeen:
                startIdx = max(startIdx, lastSeen[char] + 1)

            if longest[1] - longest[0] < endIdx + 1 - startIdx:
                longest = [startIdx, endIdx + 1]

            lastSeen[char] = endIdx
        return longest[1] - longest[0]


# Testing
class TestTwoSum(unittest.TestCase):
    def testLengthOfLongestSubstring1(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring(s="abcabcbb"), 3)

    def testLengthOfLongestSubstring2(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring(s="bbbbb"), 1)

    def testLengthOfLongestSubstring3(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring(s="pwwkew"), 3)

    def testLengthOfLongestSubstring4(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring(s=""), 0)


if __name__ == "__main__":
    unittest.main()