"""
859. Buddy Strings
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example1:
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example2:
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example3:
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:
1 <= s.length, goal.length <= 2 * 10^4
s and goal consist of lowercase letters
"""

"""
Note:
1. HashTable: O(n) time | O(n) space
"""

import collections
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        notMatches = []
        charCount = collections.Counter(s)
        for i, (sChar, gChar) in enumerate(zip(s, goal)):
            if sChar != gChar:
                notMatches.append(i)
        
        if len(notMatches) == 0:
            return True in [val >= 2 for val in charCount.values()]
        
        if len(notMatches) == 2:
            i, j = notMatches
            chars = list(s)
            chars[i], chars[j] = chars[j], chars[i]
            return "".join(chars) == goal
        
        return False


# Unit Tests
import unittest
funcs = [Solution().buddyStrings]


class TestBuddyStrings(unittest.TestCase):
    def testBuddyStrings1(self):
        for func in funcs:
            s = "ab"
            goal = "ba"
            self.assertEqual(func(s=s, goal=goal), True)

    def testBuddyStrings2(self):
        for func in funcs:
            s = "ab"
            goal = "ab"
            self.assertEqual(func(s=s, goal=goal), False)

    def testBuddyStrings3(self):
        for func in funcs:
            s = "aa"
            goal = "aa"
            self.assertEqual(func(s=s, goal=goal), True)

if __name__ == "__main__":
    unittest.main()
