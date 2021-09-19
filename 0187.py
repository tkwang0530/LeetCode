"""
187. Longest Substring Without Repeating Characters
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T' .
For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:
1 <= s.length <= 10^5
s[i] is either 'A', 'C', 'G', or 'T'.
"""

""" 
1. Two Hash Tables: O(n) time | O(n) space
"""

from typing import List
class Solution(object):
    def findRepeatedDnaSequence(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        return list(repeated)



# Unit Tests
import unittest
funcs = [Solution().findRepeatedDnaSequence]


class TestFindRepeatedDnaSequences(unittest.TestCase):
    def testFindRepeatedDnaSequences1(self):
        for func in funcs:
            s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
            self.assertEqual(sorted(func(s=s)), sorted(["AAAAACCCCC","CCCCCAAAAA"]))

    def testFindRepeatedDnaSequences2(self):
        for func in funcs:
            s = "AAAAAAAAAAAAA"
            self.assertEqual(sorted(func(s=s)), sorted(["AAAAAAAAAA"]))

if __name__ == "__main__":
    unittest.main()
