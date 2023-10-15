"""
1601. Maximum Number of Achievable Transfer Requests
description: https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/
"""

"""
Note:
1. backtracking: O(n * 2^r) time | O(r+n) space - where r is the length of array requests
"""

from typing import List
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        R = len(requests)
        
        netBuilding = [0] * n
        container = [0]
        def backtracking(i, r, netBuilding):
            if i >= R:
                if all([val == 0 for val in netBuilding]): 
                    container[0] = max(container[0], r)
                return
            backtracking(i+1, r, netBuilding)
            netBuilding[requests[i][0]] -= 1
            netBuilding[requests[i][1]] += 1
            backtracking(i+1, r+1, netBuilding)
            netBuilding[requests[i][0]] += 1
            netBuilding[requests[i][1]] -= 1

        backtracking(0, 0, netBuilding)
        return container[0]

# Unit Tests
import unittest
funcs = [Solution().maximumRequests]

class TestMaximumRequests(unittest.TestCase):
    def testMaximumRequests1(self):
        for maximumRequests in funcs:
            n = 5
            requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
            self.assertEqual(maximumRequests(n=n, requests=requests), 5)

    def testMaximumRequests2(self):
        for maximumRequests in funcs:
            n = 3
            requests = [[0,0],[1,2],[2,1]]
            self.assertEqual(maximumRequests(n=n, requests=requests), 3)

    def testMaximumRequests3(self):
        for maximumRequests in funcs:
            n = 4
            requests = [[0,3],[3,1],[1,2],[2,0]]
            self.assertEqual(maximumRequests(n=n, requests=requests), 4)

if __name__ == "__main__":
    unittest.main()