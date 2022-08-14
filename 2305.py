"""
2305. Fair Distribution of Cookies
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the i-th bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

Example1:
Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.

Example2:
Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.

Constraints:
2 <= cookies.length <= 8
1 <= cookies[i] <= 10^5
2 <= k <= cookies.length
"""

"""
Note:
1. dfs + memo: O((klogk +  k) * k**n) time | O(k * k**n) space
2. dfs + pruning: O(k * k ** n) time | O(n) space
"""
from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        groups = [0] * k
        
        memo = {}
        def dfs(startIdx, groups):
            key = str(sorted(groups)) + ";" + str(startIdx)
            if key in memo:
                return memo[key]
            if startIdx == n:
                return max(groups)
            
            ans = float("inf")
            cookie = cookies[startIdx]
            
            for i in range(k):
                groups[i] += cookie
                ans = min(ans, dfs(startIdx+1, groups))
                groups[i] -= cookie
                
            memo[key] = ans
            return memo[key]
        return dfs(0, groups)

    def distributeCookies2(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        groups = [0] * k

        def dfs(startIdx):
            if startIdx == n:
                return max(groups)
            
            ans = float("inf")
            cookie = cookies[startIdx]
            for i in range(k):
                groups[i] += cookie
                ans = min(ans, dfs(startIdx+1))
                groups[i] -= cookie
                if groups[i] == 0:
                    break

            return ans
        return dfs(0)

# Unit Tests
import unittest
funcs = [Solution().distributeCookies, Solution().distributeCookies2]

class TestDistributeCookies(unittest.TestCase):
    def testDistributeCookies1(self):
        for func in funcs:
            cookies = [8,15,10,20,8]
            k = 2
            self.assertEqual(func(cookies=cookies, k=k), 31)

    def testDistributeCookies2(self):
        for func in funcs:
            cookies = [6,1,3,2,2,4,1,2]
            k = 3
            self.assertEqual(func(cookies=cookies, k=k), 7)

if __name__ == "__main__":
    unittest.main()