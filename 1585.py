"""
1585. Check If String Is Transformable With Substring Sort Operations
description: https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/description/
"""

"""
Note:
1. Greedy + Stack: O(n) time | O(n) space - where n is the length of string s
ref: https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/solutions/843917/c-java-python-o-n/
"""
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        index = [[] for _ in range(10)]
        for i in range(len(s)-1, -1, -1):
            index[int(s[i])].append(i)

        for char in t:
            digit = int(char)
            if not index[digit]:
                return False

            for k in range(digit):
                if index[k] and index[k][-1] < index[digit][-1]:
                    return False

            index[digit].pop()
        return True

# Unit Tests
import unittest
funcs = [Solution().isTransformable]

class TestIsTransformable(unittest.TestCase):
    def testIsTransformable1(self):
        for func in funcs:
            s = "84532"
            t = "34852"
            self.assertEqual(func(s=s, t=t), True)

    def testIsTransformable2(self):
        for func in funcs:
            s = "34521"
            t = "23415"
            self.assertEqual(func(s=s, t=t), True)

    def testIsTransformable3(self):
        for func in funcs:
            s = "12345"
            t = "12435"
            self.assertEqual(func(s=s, t=t), False)

if __name__ == "__main__":
    unittest.main()