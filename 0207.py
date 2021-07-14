"""
207. Course Schedule
There are total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 10^5
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
"""

"""
Note:
1. DFS Topological Sort: O(V+E) time | O(V+E) space 
"""




import unittest
from typing import List
class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        for _ in range(numCourses):
            graph.append([])
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visited = [0] * numCourses
        for i in range(numCourses):
            if self.dfs(i, graph, visited):
                return False
        return True

    def dfs(self, i, graph, visited):
        if visited[i] == 1:
            return True
        if visited[i] == 2:
            return False
        visited[i] = 1
        for j in graph[i]:
            if self.dfs(j, graph, visited):
                return True
        visited[i] = 2
        return False

    # Unit Tests
funcs = [Solution().canFinish]


class TestCanFinish(unittest.TestCase):
    def testCanFinish1(self):
        for func in funcs:
            numCourses = 2
            prerequisites = [[1, 0]]
            self.assertEqual(
                func(numCourses=numCourses, prerequisites=prerequisites), True)

    def testCanFinish2(self):
        for func in funcs:
            numCourses = 2
            prerequisites = [[1, 0], [0, 1]]
            self.assertEqual(
                func(numCourses=numCourses, prerequisites=prerequisites), False)


if __name__ == "__main__":
    unittest.main()
