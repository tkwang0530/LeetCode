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
Detect Loop in the graph

2. DFS: O(V+E) time | O(V+E) space
remove finish course from the prerequisites list
"""

import unittest
from typing import List, Dict, Set
class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        for _ in range(numCourses):
            graph.append([])
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        # mark all the course as 0 (unknown) as a start
        visited = [0] * numCourses
        for course in range(numCourses):
            if self.dfs(course, graph, visited):
                return False
        return True

    def dfs(self, course: int, graph: List[List[int]], visited: Set[int]):
        # because we are visiting the course, and we meet the course again, meaning we have a loop
        if visited[course] == 1:
            return True

        # because we have visited the course, return False
        # that is, there is no Loop start from that course
        if visited[course] == 2:
            return False
        visited[course] = 1
        for prerequisite in graph[course]:
            if self.dfs(prerequisite, graph, visited):
                return True
        
        # after finish dfs on the course we mark the course as 2, meaning we have visited the course
        visited[course] = 2
        return False

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prerequisites List
        graph = { course:[] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        # visited = all courses along the current DFS path
        visited = set()
        for course in range(numCourses):
            if not self.dfs2(course, graph, visited):
                return False
        return True
    
    def dfs2(self, course: int, graph: Dict[int, List[int]], visited: Set[int]) -> bool:
        if course in visited:
            return False
        if len(graph[course]) == 0:
            return True
        visited.add(course)
        for prerequisite in graph[course]:
            if not self.dfs2(prerequisite, graph, visited):
                return False
        visited.remove(course)
        graph[course] = []
        return True

    # Unit Tests
funcs = [Solution().canFinish, Solution().canFinish2]


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
