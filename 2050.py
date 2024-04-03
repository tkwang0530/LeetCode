"""
2050. Parallel Courses III
description: https://leetcode.com/problems/parallel-courses-iii/description/
"""

"""
Note:
1. Topological Sort: O(N+E) time | O(N+E) space - where N is the number of courses and E is the number of edges
ref: https://leetcode.com/problems/parallel-courses-iii/solutions/1537479/c-python-topology-sort-o-m-n-clean-concise
"""

import collections
from typing import List
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(list)
        inDegree = [0] * n
        for prereq, course in relations:
            # convert into zero based index
            prereq, course = prereq-1, course-1

            graph[prereq].append(course)
            inDegree[course] += 1

        queue = collections.deque([])
        dist = [0] * n
        for course in range(n):
            if inDegree[course] == 0:
                queue.append(course)
                dist[course] = time[course]

        while queue:
            prereq = queue.popleft()
            for course in graph[prereq]:
                dist[course] = max(dist[prereq]+time[course], dist[course])
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        return max(dist)

# Unit Tests
import unittest
funcs = [Solution().minimumTime]

class TestMinimumTime(unittest.TestCase):
    def testMinimumTime1(self):
        for minimumTime in funcs:
            n = 3
            relations = [[1,3],[2,3]]
            time = [3,2,5]
            self.assertEqual(minimumTime(n=n, relations=relations, time=time), 8)

    def testMinimumTime2(self):
        for MinimumTime in funcs:
            n = 5
            relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
            time = [1,2,3,4,5]
            self.assertEqual(MinimumTime(n=n, relations=relations, time=time), 12)

if __name__ == "__main__":
    unittest.main()