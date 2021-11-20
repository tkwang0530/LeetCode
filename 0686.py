"""
686. Repeated String Match
Given two strings a and b, return the minimum number of times you should repeat string a so that b is a substring of it. If it is impossible for b to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".


Example1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example2:
Input: a = "a", b = "aa"
Output: 2

Example3:
Input: a = "a", b = "a"
Output: 1

Example4:
Input: a = "abc", b = "wxyz"
Output: -1

Constraints:
1 <= a.length <= 10^4
1 <= b.length <= 10^4
a and b consist of lower-case English letters.
"""

""" 
Note:
1. Rolling hash: O(n+m) time | O(n+m) space - where n is len(a) and m is len(b)
aka Rabin-Karp with Rabin fingerprint

Rabin fingerprinting scheme
Given an n-bit message s_0, ..., s_n-1
hash(s) = s_0 + s_1 * p + ... + s_n-1 * p^(n-1), where p is a prime and p > n

hash(s) could be very large => using modulus hash(s) % m, where m is a large prime (e.g. 1000,000,007)

2. Rolling hash without modulus (python only): O(n+m) time | O(1) space - where n is len(a) and m is len(b)
"""

class Solution(object):
    def repeatedStringMatch(self, a: str, b: str) -> int:
        base, mod = 31, 10 ** 9 + 7
        maxLength = len(a) + len(b)
        hashB = ord(b[0])
        hashA = [0] * maxLength
        hashA[0] = ord(a[0])
        basePower = base

        for i in range(1, len(b)):
            hashB = (hashB * base) % mod + ord(b[i])
            hashA[i] = (hashA[i-1] * base) % mod + ord(a[i % len(a)])

            basePower = (basePower * base) % mod
        
        if hashA[len(b) - 1] == hashB:
            return len(b) // len(a) if len(b) % len(a) == 0 else len(b) // len(a) + 1
        
        for i in range(len(b), maxLength):
            leftChar, rightChar = a[(i-len(b)) % len(a)], a[i % len(a)]
            hashA[i] = (hashA[i-1] * base) % mod + ord(rightChar)
            hashA[i] = hashA[i] + mod - (basePower * ord(leftChar)) % mod

            if hashA[i] % mod == hashB:
                return (i+1) // len(a) if (i+1) % len(a) == 0 else (i+1) // len(a) + 1
        return -1

    def repeatedStringMatch2(self, a: str, b: str) -> int:
        base = 31
        maxLength = len(a) + len(b)
        hashB = ord(b[0])
        hashA = ord(a[0])
        basePower = base
        
        for i in range(1, len(b)):
            hashB = hashB * base + ord(b[i])
            hashA = hashA * base + ord(a[i % len(a)])
            basePower = basePower * base
            
        if hashA == hashB:
            return len(b) // len(a) if len(b) % len(a) == 0 else len(b) // len(a) + 1
        
        for i in range(len(b), maxLength):
            leftChar, rightChar = a[(i - len(b)) % len(a)], a[i % len(a)]
            hashA = hashA * base + ord(rightChar) - basePower * ord(leftChar)
            
            if hashA == hashB:
                return (i+1) // len(a) if (i+1) % len(a) == 0 else (i+1) // len(a) + 1
        return -1

# Unit Tests
import unittest
funcs = [Solution().repeatedStringMatch, Solution().repeatedStringMatch2]

class TestRepeatedStringMatch(unittest.TestCase):
    def testRepeatedStringMatch1(self):
        for func in funcs:
            self.assertEqual(func(a="abcd", b="cdabcdab"), 3)

    def testRepeatedStringMatch2(self):
        for func in funcs:
            self.assertEqual(func(a="a", b="aa"), 2)

    def testRepeatedStringMatch3(self):
        for func in funcs:
            self.assertEqual(func(a="a", b="a"), 1)

    def testRepeatedStringMatch4(self):
        for func in funcs:
            self.assertEqual(func(a="abc", b="wxyz"), -1)

    def testRepeatedStringMatch5(self):
        for func in funcs:
            self.assertEqual(func(a="aaac", b="aac"), 1)

    def testRepeatedStringMatch6(self):
        for func in funcs:
            self.assertEqual(func(a="abc", b="cabcabca"), 4)


if __name__ == "__main__":
    unittest.main()
