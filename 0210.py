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
2. BFS Topological Sort: O(V+E) time | O(V+E) space
3. BFS Topological Sort (improved): O(V+E) time | O(V+E) space
"""


from collections import defaultdict, deque
from typing import List

class Node:
    def __init__(self, id):
        self.id = id
        self.preCourseCounts = 0
        self.parentCourses = []
class Solution(object):
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for course in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visited = [0] * numCourses
        order = []
        for course in range(numCourses):
            if self.dfs(course, graph, visited, order):
                return []
        return order

    def dfs(self, course: int, graph: List[List[int]], visited: List[int], order: List[int]) -> bool:
        if visited[course] == 1:
            return True
        if visited[course] == 2:
            return False
        visited[course] = 1
        for prerequisite in graph[course]:
            if self.dfs(prerequisite, graph, visited, order):
                return True
        visited[course] = 2
        order.append(course)
        return False

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a prerequisite dict. (containing courses that need to be taken (visit))
        # before we can visit the key itself
        prerequisitesDict = { course: set() for course in range(numCourses)}
        graph = defaultdict(set)
        for course, prerequisite in prerequisites:
            # prerequisitesDict store requiements as their given
            prerequisitesDict[course].add(prerequisite)
            # Graph stores courses and its neighbor
            graph[prerequisite].add(course)

        queue = deque([])

        # we need to find a starting location, aka courses that have no prerequisites
        for course, preCourses in prerequisitesDict.items():
            if len(preCourses) == 0:
                queue.append(course)
        
        # Keep track of which courses have been taken.
        taken = []
        while len(queue) > 0:
            course = queue.popleft()
            taken.append(course)

            # If we have visited the numCourses we're done.
            if len(taken) == numCourses:
                return taken
            
            # For neighboring courses
            for neighbor in graph[course]:
                # If the course we've just taken was a preCourse for the next course, remove it from its preCourses list
                prerequisitesDict[neighbor].remove(course)
                # If we've taken all of the preCourses for the new course, we'll visit it.
                if len(prerequisitesDict[neighbor]) == 0:
                    queue.append(neighbor)
        return [] 

    def findOrder3(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preCourseCounts = [0] * numCourses
        graph = [[] for course in range(numCourses)]
        for course, prerequisite in prerequisites:
            preCourseCounts[course] += 1
            graph[prerequisite].append(course)
        queue = deque([])
        for course, counts in enumerate(preCourseCounts):
            if counts == 0:
                queue.append(course)     
        taken = []
        while len(queue) > 0:
            course = queue.popleft()
            taken.append(course)
            if len(taken) == numCourses:
                return taken
            for neighbor in graph[course]:
                preCourseCounts[neighbor] -= 1
                if preCourseCounts[neighbor] == 0:
                    queue.append(neighbor)
        return []

    def findOrder4(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {id: Node(id) for id in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].preCourseCounts += 1
            graph[prerequisite].parentCourses.append(graph[course])
            
        queue = deque([])
        for course in range(numCourses):
            if graph[course].preCourseCounts == 0:
                queue.append(graph[course])
        
        taken = []
        while len(queue) > 0:
            node = queue.popleft()
            taken.append(node.id)
            if len(taken) == numCourses:
                return taken
            for parentCourse in node.parentCourses:
                parentCourse.preCourseCounts -= 1
                if parentCourse.preCourseCounts == 0:
                    queue.append(parentCourse)
        return []

# Unit Tests
import unittest
funcs = [Solution().findOrder, Solution().findOrder2, Solution().findOrder3, Solution().findOrder4]
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

    def testFindOrder4(self):
        for func in funcs:
            numCourses = 2
            prerequisites = [[0,1]]
            self.assertEqual(
                func(numCourses=numCourses, prerequisites=prerequisites), [1,0])


if __name__ == "__main__":
    unittest.main()
