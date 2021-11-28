"""
299. Bulls and Cows
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Example3:
Input: secret = "1", guess = "0"
Output: "0A0B"

Example4:
Input: secret = "1", guess = "1"
Output: "1A0B"

Constraints:
1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
"""

""" 
1. intersec of HashTable: O(n) time | O(1) space - where n is the length of secret
"""



import collections
class Solution(object):
    def getHint(self, secret: str, guess: str) -> str:
        countA = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
        intersecCharCount = collections.Counter(guess) & collections.Counter(secret)
        return f"{countA}A{sum(intersecCharCount.values()) - countA}B"


# Unit Tests
import unittest
funcs = [Solution().getHint]


class TestGetHint(unittest.TestCase):
    def testGetHint1(self):
        for func in funcs:
            secret = "1807"
            guess = "7810"
            self.assertEqual(func(secret=secret, guess=guess), "1A3B")

    def testGetHint2(self):
        for func in funcs:
            secret = "1123"
            guess = "0111"
            self.assertEqual(func(secret=secret, guess=guess), "1A1B")

    def testGetHint3(self):
        for func in funcs:
            secret = "1"
            guess = "0"
            self.assertEqual(func(secret=secret, guess=guess), "0A0B")

    def testGetHint4(self):
        for func in funcs:
            secret = "1"
            guess = "1"
            self.assertEqual(func(secret=secret, guess=guess), "1A0B")


if __name__ == "__main__":
    unittest.main()
