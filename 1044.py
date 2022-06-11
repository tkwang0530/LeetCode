"""
1044. Longest Duplicate Substring
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example1:
Input: s = "banana"
Output: "ana"

Example2:
Input: s = "abcd"
Output: ""

Constraints:
2 <= s.length <= 3 * 10^4
s consists of lowercase English letters.
"""

"""
Note:
1. Rolling Hash + Binary Search: O(nlogn) time | O(n^2) space
"""

import unittest, collections
from typing import List
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        MOD = 2**32
        a = 26
        n = len(s)
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i-1] * a) % MOD
        
        # map characters into numbers
        nums = [ord(char) - ord('a') for char in s]
        def search(L: int, nums: List[int]) -> int:
            h = 0

            # calculate the initial window hash value
            for i in range(L):
                h = (h * a + nums[i]) % MOD

            hashStartIndice = collections.defaultdict(list)
            hashStartIndice[h].append(0)
            for start in range(1, n-L+1):
                h = h * a  # move window
                h = (h - nums[start - 1] * power[L] % MOD + MOD) % MOD  # remove tail digit
                h = (h + nums[start + L - 1]) % MOD # add new head digit
                for i in hashStartIndice[h]:
                    if nums[i:i+L] == nums[start:start+L]:
                        return i
                hashStartIndice[h].append(start)
            return -1

        left, right = 1, n
        maxLength = 0
        while left < right:
            mid = left + (right - left) // 2
            startIndex = search(mid, nums)
            if startIndex == -1:
                right = mid
            else:
                maxLength = max(maxLength, mid)
                left = mid + 1
        
        if maxLength == 0:
            return ""
        startIndex = search(maxLength, nums)
        return s[startIndex: startIndex+maxLength]


# Unit Tests
funcs = [Solution().longestDupSubstring]


class TestLongestDupSubstring(unittest.TestCase):
    def testLongestDupSubstring1(self):
        for func in funcs:
            s = "banana"
            self.assertEqual(func(s=s), "ana")

    def testLongestDupSubstring2(self):
        for func in funcs:
            s = "abcd"
            self.assertEqual(func(s=s), "")

    def testLongestDupSubstring3(self):
        for func in funcs:
            s = "aa"
            self.assertEqual(func(s=s), "a")

if __name__ == "__main__":
    unittest.main()
