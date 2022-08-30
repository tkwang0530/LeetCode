"""
1461. Check if a String Contains All Binary Codes of Size K
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

Example2:
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

Example3:
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:
1 <= s.length <= 5 * 10^5
s[i] is either '0' or '1'.
1 <= k <= 20
"""

"""
Note:
1. Rolling Hash: O(n+k) time | O(2**k) space
"""

import collections
from typing import List
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 2**k:
            return False
        MOD = 10**9 + 7
        
        # how many kinds of s[i] -> a
        a = 2
        
        n = len(s)
        power = [1] * (k+1)
        for i in range(1, k+1):
            power[i] = (power[i-1] * a) % MOD
        
        def search(L: int, nums: List[int]) -> int:
            h = 0
            
            # calculate the initial window hash value
            for i in range(L):
                h = (h * a + nums[i]) % MOD
                
            hashStartIndice = collections.defaultdict(list)
            hashStartIndice[h].append(0)
            for start in range(1, n-L+1):
                h = h * a # move window
                h = (h - nums[start-1] * power[L] % MOD + MOD) % MOD # remove tail digit
                h = (h + nums[start+L-1]) % MOD # add new head digit
                hasFoundMatch = False
                for i in hashStartIndice[h]:
                    if nums[i:i+L] == nums[start:start+L]:
                        hasFoundMatch = True
                        break
                if not hasFoundMatch:
                    hashStartIndice[h].append(start)
            return sum([len(arr) for arr in hashStartIndice.values()])
        
        nums = [int(char) for char in s]
        return search(k, nums) == 2**k

# Unit Tests
import unittest
funcs = [Solution().hasAllCodes]
class TestHasAllCodes(unittest.TestCase):
    def testHasAllCodes1(self):
        for func in funcs:
            s = "00110110"
            k = 2
            self.assertEqual(func(s=s, k=k), True)

    def testHasAllCodes2(self):
        for func in funcs:
            s = "0110"
            k = 1
            self.assertEqual(func(s=s, k=k), True)

    def testHasAllCodes3(self):
        for func in funcs:
            s = "0110"
            k = 2
            self.assertEqual(func(s=s, k=k), False)

if __name__ == "__main__":
    unittest.main()
