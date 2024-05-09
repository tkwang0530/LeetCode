
"""
1017. Convert to Base -2
description: https://leetcode.com/problems/convert-to-base-2/description/
"""

"""
Note:
1. like base2: O(logn) time | O(logn) space
ref: https://leetcode.com/problems/convert-to-base-2/solutions/265507/java-c-python-2-lines-exactly-same-as-base-2
"""

class Solution:
    def baseNeg2(self, n: int) -> str:
        output = []
        while n:
            output.append(n & 1)
            n = -(n >> 1)

        outputStr = "0" if not output else ("".join([str(b) for b in output[::-1]]))
        return outputStr

# Unit Tests
import unittest
funcs = [Solution().baseNeg2]

class TestBaseNeg2(unittest.TestCase):
    def testBaseNeg2_1(self):
        for baseNeg2 in funcs:
            n = 2
            self.assertEqual(baseNeg2(n=n), "110")

    def testBaseNeg2_2(self):
        for baseNeg2 in funcs:
            n = 3
            self.assertEqual(baseNeg2(n=n), "111")

    def testBaseNeg2_3(self):
        for baseNeg2 in funcs:
            n = 4
            self.assertEqual(baseNeg2(n=n), "100")


if __name__ == "__main__":
    unittest.main()