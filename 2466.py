"""
2466. Count Ways To Build Good Strings
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 10^9 + 7.

Example1:
Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.

Example2:
Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".

Constraints:
1 <= low <= high <= 10^5
1 <= zero, one <= low
"""

"""
Note:
1. dfs+memo: O(high) time | O(high) space
2. dp: O(high) time | O(high) space
"""

import unittest, functools
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @functools.lru_cache(None)
        def dfs(L, H):
            if H < 0:
                return 0
            elif H == 0:
                return 1
            else:
                return (L <= 0) + dfs(L-zero, H-zero) + dfs(L-one, H-one)

        return dfs(low, high) % (10**9 + 7)
    
    def countGoodStrings2(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1
        total = 0
        mod = 10**9 + 7
        for i in range(1, high+1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i-zero]) % mod
            if i >= one:
                dp[i] = (dp[i] + dp[i-one]) % mod
            if i >= low:
                total = (total + dp[i]) % mod
        return total


# Unit Tests
funcs = [Solution().countGoodStrings, Solution().countGoodStrings2]


class TestCountGoodStrings(unittest.TestCase):
    def testCountGoodStrings1(self):
        for func in funcs:
            low = 3
            high = 3
            zero = 1
            one = 1
            self.assertEqual(func(low=low, high=high, zero=zero, one=one), 8)

    def testCountGoodStrings2(self):
        for func in funcs:
            low = 2
            high = 3
            zero = 1
            one = 2
            self.assertEqual(func(low=low, high=high, zero=zero, one=one), 5)


if __name__ == "__main__":
    unittest.main()
