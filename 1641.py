"""
1641. Count Sorted Vowel Strings
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example3:
Input: n = 33
Output: 66045

Constraints:
1 <= n <= 50
"""

"""
Note:
1. Math: O(n) time | O(n) space
H(n, m): n same objects to m different objects
H(n, m) = C(n+m-1, m)
C(n, m) = n! / [(n-m)!*m!]
"""

class Solution:
    def countVowelStrings(self, n: int) -> int:
        same = n
        diff = 5

        memo = {}
        def factor(n):
            if n in memo:
                return memo[n]
            result = 1
            for i in range(1, n+1):
                result *= i
            memo[n] = result
            return memo[n]

        def combination(n, m):
            child = factor(n)
            parent = factor(n-m) * factor(m)
            return child // parent

        def multiCombination(n, m):
            return combination(n+m-1, m)

        return multiCombination(diff, same)

# Unit Tests
import unittest
funcs = [Solution().countVowelStrings]

class TestCountVowelStrings(unittest.TestCase):
    def testCountVowelStrings1(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), 5)

    def testCountVowelStrings2(self):
        for func in funcs:
            n = 2
            self.assertEqual(func(n=n), 15)

    def testCountVowelStrings3(self):
        for func in funcs:
            n = 33
            self.assertEqual(func(n=n), 66045)

    def testCountVowelStrings4(self):
        for func in funcs:
            n = 3
            self.assertEqual(func(n=n), 35)


if __name__ == "__main__":
    unittest.main()
