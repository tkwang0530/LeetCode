"""
210. Course Schedule II
There are total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


Example1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
"""

"""
Note:
1. DFS Topological Sort: O(V+E) time | O(V+E) space 
"""




import unittest
from typing import List
class Solution(object):
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = []
        for _ in range(numCourses):
            graph.append([])
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visited = [0] * numCourses
        order = []
        for i in range(numCourses):
            if self.dfs(i, graph, visited, order):
                return []
        return order

    def dfs(self, i, graph, visited, order):
        if visited[i] == 1:
            return True
        if visited[i] == 2:
            return False
        visited[i] = 1
        for j in graph[i]:
            if self.dfs(j, graph, visited, order):
                return True
        visited[i] = 2
        order.append(i)
        return False


    # Unit Tests
funcs = [Solution().findOrder]


class TestFindOrder(unittest.TestCase):
    def testFindOrder1(self):
        for func in funcs:
            numCourses = 2
            prerequisites = [[1, 0]]
            self.assertEqual(
                func(numCourses=numCourses, prerequisites=prerequisites), [0, 1])

    def testFindOrder2(self):
        for func in funcs:
            numCourses = 4
            prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
            self.assertEqual(
                func(numCourses=numCourses, prerequisites=prerequisites), [0, 1, 2, 3])

    def testFindOrder3(self):
        for func in funcs:
            numCourses = 1
            prerequisites = []
            self.assertEqual(
                func(numCourses=numCourses, prerequisites=prerequisites), [0])


if __name__ == "__main__":
    unittest.main()
