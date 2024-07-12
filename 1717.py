"""
1717. Maximum Score From Removing Substrings
description: https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
"""

"""
Note:
1. Greedy + Stack: O(n) time | O(n) space - where n is the length of the string s
ref: https://www.youtube.com/watch?v=r_3a0oG1VcY
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removePairs(pair, score):
            nonlocal s
            result = 0
            stack = []
            for char in s:
                if char == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    result += score
                else:
                    stack.append(char)
            
            s = "".join(stack)
            return result

        output = 0
        pair = "ab" if x > y else "ba"
        output += removePairs(pair, max(x,y))
        output += removePairs(pair[::-1], min(x,y))
        return output

# Unit Tests
import unittest
funcs = [Solution().maximumGain]

class TestMaximumGain(unittest.TestCase):
    def testMaximumGain1(self):
        for func in funcs:
            s = "cdbcbbaaabab"
            x = 4
            y = 5
            self.assertEqual(func(s=s, x=x, y=y), 19)

    def testMaximumGain2(self):
        for func in funcs:
            s = "aabbaaxybbaabb"
            x = 5
            y = 4
            self.assertEqual(func(s=s, x=x, y=y), 20)

if __name__ == "__main__":
    unittest.main()