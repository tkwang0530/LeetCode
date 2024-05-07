"""
816. Ambiguous Coordinates
description: https://leetcode.com/problems/ambiguous-coordinates/description/
"""

"""
Note:
1. backtrack: O(2^n * n) time | O(2^n * n) space - where n is the length of string s
"""




from typing import List
import unittest
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:len(s)-1]
        n = len(s)
        def isValidNumberStr(numStr: str) -> bool:
            parts = numStr.split(".")
            if len(parts) > 2:
                return False
            if len(parts) == 1:
                # check empty string
                if parts[0] == "":
                    return False

                # check leading zero
                if len(parts[0]) >= 2 and parts[0][0] == "0":
                    return False
            else:
                # check empty string
                if "" in parts:
                    return False

                # left check leading zero
                if len(parts[0]) >= 2 and parts[0][0] == "0":
                    return False
                
                # right check ending zero
                if parts[1][-1] == "0":
                    return False
            return True
        def isValid(candidate: str) -> bool:
            parts = candidate.split(", ")
            if len(parts) != 2:
                return False
            numStr1, numStr2 = parts
            return isValidNumberStr(numStr1) and isValidNumberStr(numStr2)

        output = set()
        current = []
        def dfs(i, c, p):
            if i == n:
                if c == 0:
                    candidate = "".join(current)
                    if isValid(candidate):
                        output.add(candidate)
                return
            
            # skip all, append char only
            current.append(s[i])
            dfs(i+1, c, p)
            current.pop()

            # use c if c > 0
            if c > 0:
                current.append(", ")
                dfs(i, c-1, p)
                current.pop()

            # use p if p > 0
            if p > 0:
                current.append(".")
                dfs(i, c, p-1)
                current.pop()
        dfs(0, 1, 2)
        return ["("+candidate+")" for candidate in output]



# Unit Tests
funcs = [Solution().ambiguousCoordinates]


class TestAmbiguousCoordinates(unittest.TestCase):
    def testAmbiguousCoordinates1(self):
        for func in funcs:
            s = "(123)"
            self.assertEqual(set(func(s=s)), set(["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]))

    def testAmbiguousCoordinates2(self):
        for func in funcs:
            s = "(00011)"
            self.assertEqual(set(func(s=s)), set(["(0.001, 1)","(0, 0.011)"]))

    def testAmbiguousCoordinates3(self):
        for func in funcs:
            s = "(0123)"
            self.assertEqual(set(func(s=s)), set(["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]))


if __name__ == "__main__":
    unittest.main()
