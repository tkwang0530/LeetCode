"""
1376. Time Needed to Inform All Employees
description: https://leetcode.com/problems/time-needed-to-inform-all-employees/description/
"""

"""
Note:
1. BFS (layerOrder Traversal): O(n) time | O(n) space - where n is the number of nodes in the tree
2. DFS (postOrder Traversal): O(n) time | O(n+h) space - where n is the number of node in the tree and h is the height of the tree
"""

from typing import List
import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        empolyeeDegree = collections.defaultdict(int)
        dp = collections.defaultdict(int)

        for employeeID in range(n):
            dp[employeeID] = informTime[employeeID]
            managerID = manager[employeeID]
            if managerID != -1:
                empolyeeDegree[managerID] += 1
        
        currentEmployees = []
        for employeeID in range(n):
            if empolyeeDegree[employeeID] == 0:
                currentEmployees.append(employeeID)
        
        while currentEmployees:
            nextEmployees = []
            for employeeID in currentEmployees:
                managerID = manager[employeeID]
                if managerID == -1:
                    continue
                empolyeeDegree[managerID] -= 1
                dp[managerID] = max(dp[managerID], informTime[managerID]+dp[employeeID])
                if empolyeeDegree[managerID] == 0:
                    nextEmployees.append(managerID)
            
            currentEmployees = nextEmployees

        return dp[headID]

class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employeeDegree = collections.defaultdict(int)
        ds = collections.defaultdict(list)
        for employeeID in range(n):
            managerID = manager[employeeID]
            if managerID == -1:
                continue
            employeeDegree[managerID] += 1
            ds[managerID].append(employeeID)
        def dfs(employeeID):
            if employeeDegree[employeeID] == 0:
                return 0

            time = informTime[employeeID]
            for e in ds[employeeID]:
                time = max(time, dfs(e)+informTime[employeeID])
            
            return time

        return dfs(headID)

# Unit Tests
import unittest
funcs = [Solution().numOfMinutes, Solution2().numOfMinutes]
class TestNumOfMinutes(unittest.TestCase):
    def testNumOfMinutes1(self):
        for numOfMinutes in funcs:
            n = 1
            headID = 0
            manager = [-1]
            informTime = [0]
            self.assertEqual(numOfMinutes(n=n, headID=headID, manager=manager, informTime=informTime), 0)

    def testNumOfMinutes2(self):
        for numOfMinutes in funcs:
            n = 6
            headID = 2
            manager = [2,2,-1,2,2,2]
            informTime = [0,0,1,0,0,0]
            self.assertEqual(numOfMinutes(n=n, headID=headID, manager=manager, informTime=informTime), 1)

if __name__ == "__main__":
    unittest.main()
