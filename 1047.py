"""
1047. Remove All Adjacent Duplicates In String
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example2:
Input: s = "azxxzy"
Output: "ay"

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""

"""
Note:
1. Using Stack: O(n) time | O(n-d) space
where d is the length of duplicates
if len(stack) > 0 and stack[len(stack) - 1] == char, stack.pop()
otherwise, stack.append(char)
"""

from typing import List
import unittest
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)



# Unit Tests
funcs = [Solution().removeDuplicates]


class TestRemoveDuplicates(unittest.TestCase):
    def testRemoveDuplicates1(self):
        for func in funcs:
            s = "abbaca"
            self.assertEqual(func(s=s), "ca")

    def testRemoveDuplicates2(self):
        for func in funcs:
            s = "azxxzy"
            self.assertEqual(func(s=s), "ay")

if __name__ == "__main__":
    unittest.main()
