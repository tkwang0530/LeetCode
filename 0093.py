"""
93. Restore IP Addresses
Given a string s containing only digits, return all possible valid IP address that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Example1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example3:
Input: s = "1111"
Output: ["1.1.1.1"]

Example4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
0 <= s.length <= 3000
s consists of digits only.
"""

""" 
1. Recursive DFS (Backtracking): O(1) time | O(1) space
"""

from typing import List
class Solution(object):
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 256 choices for each of the 4 spots BUT ...
        # The order of s stays same,
        # we just place the "." in between

        result = []
        if len(s) > 12:
            return result
        self.dfs(s, 0, 0, "", result)
        return result

    def dfs(self, s: str, i: int, dots: int, currentIP: str, result: List[str]) -> None:
        if dots == 4 and i == len(s):
            result.append(currentIP[:-1])
            return
        if dots > 4:
            return
        
        for j in range(i, min(i+3, len(s))):
            numStr = s[i:j+1]
            if int(numStr) < 256 and (i == j or s[i] != "0"):
                self.dfs(s, j+1, dots+1, currentIP + numStr + ".",  result)


# Unit Tests
import unittest
funcs = [Solution().restoreIpAddresses]


class TestRestoreIpAddresses(unittest.TestCase):
    def testRestoreIpAddresses1(self):
        for func in funcs:
            s = "25525511135"
            self.assertEqual(sorted(func(s=s)), sorted(["255.255.11.135","255.255.111.35"]))

    def testRestoreIpAddresses2(self):
        for func in funcs:
            s = "0000"
            self.assertEqual(sorted(func(s=s)), sorted(["0.0.0.0"]))

    def testRestoreIpAddresses3(self):
        for func in funcs:
            s = "1111"
            self.assertEqual(sorted(func(s=s)), sorted(["1.1.1.1"]))

    def testRestoreIpAddresses4(self):
        for func in funcs:
            s = "010010"
            self.assertEqual(sorted(func(s=s)), sorted(["0.10.0.10","0.100.1.0"]))

    def testRestoreIpAddresses5(self):
        for func in funcs:
            s = "101023"
            self.assertEqual(sorted(func(s=s)), sorted(["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]))

if __name__ == "__main__":
    unittest.main()
