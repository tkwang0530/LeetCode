"""
1462. Course Schedule IV
description: https://leetcode.com/problems/course-schedule-iv/description/
"""

"""
Note:
1. DFS + memo: O(n^3) time | O(n^2) space
"""

import collections, functools
from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build prevCourse graph
        graph = collections.defaultdict(list)
        for prev, course in prerequisites:
            graph[prev].append(course)
        
        
        @functools.lru_cache(None)
        def dfs(prev, course):
            if prev == course:
                return True

            isPrerequisite = False
            for c in graph[prev]:
                isPrerequisite |= dfs(c, course)
            return isPrerequisite
        
        output = []
        for query in queries:
            output.append(dfs(query[0], query[1]))
            
        return output

# Unit Tests
import unittest
funcs = [Solution().checkIfPrerequisite]

class TestCheckIfPrerequisite(unittest.TestCase):
    def testCheckIfPrerequisite1(self):
        for func in funcs:
            numCourses = 2
            prerequisites = [[1,0]]
            queries = [[0,1],[1,0]]
            self.assertEqual(func(numCourses=numCourses, prerequisites=prerequisites, queries=queries), [False,True])

    def testCheckIfPrerequisite2(self):
        for func in funcs:
            numCourses = 2
            prerequisites = []
            queries = [[1,0],[0,1]]
            self.assertEqual(func(numCourses=numCourses, prerequisites=prerequisites, queries=queries), [False,False])

    def testCheckIfPrerequisite3(self):
        for func in funcs:
            numCourses = 3
            prerequisites = [[1,2],[1,0],[2,0]]
            queries = [[1,0],[1,2]]
            self.assertEqual(func(numCourses=numCourses, prerequisites=prerequisites, queries=queries), [True,True])

if __name__ == "__main__":
    unittest.main()