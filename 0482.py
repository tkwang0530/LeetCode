"""
482. License Key Formatting
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.


Example2:
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

Constraints:
1 <= s.length <= 10^5
s consists of English letters, digits, and dashes '-'.
1 <= k <= 10^4
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space - where n is the length of s
"""




import unittest
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        newStr = "".join([char if char != "-" else "" for char in s])
        count = 0
        output = []
        for i in range(len(newStr)-1, -1, -1):
            char = newStr[i]
            if char.isalpha():
                char = char.upper()
            output.append(char)
            count += 1
            if count == k:
                output.append("-")
                count = 0

        if output and output[-1] == "-":
            output.pop()

        return "".join(output[::-1])


# Unit Tests
funcs = [Solution().licenseKeyFormatting]


class TestLicenseKeyFormatting(unittest.TestCase):
    def testLicenseKeyFormatting1(self):
        for func in funcs:
            s = "5F3Z-2e-9-w"
            k = 4
            self.assertEqual(func(s=s, k=k), "5F3Z-2E9W")

    def testLicenseKeyFormatting2(self):
        for func in funcs:
            s = "2-5g-3-J"
            k = 2
            self.assertEqual(func(s=s, k=k), "2-5G-3J")


if __name__ == "__main__":
    unittest.main()
