"""
1136. Parallel Courses
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

Example1:
Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.

Example2:
Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.

Constraints:
1 <= n <= 5000
1 <= relations.length <= 5000
relations[i].length == 2
1 <= prevCourse_i, nextCourse_i <= n
prevCourse_i != nextCourse_i
All the pairs [prevCourse_i, nextCouse_i] are unique.
"""

"""
Note:
1. topological sort: O(V+E) time | O(V+E) space - where V is the number of course and E is the length of array relations
"""

import unittest, collections
from typing import List
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        coursePrevCoursesMap = collections.defaultdict(set)
        courseNextCoursesMap = collections.defaultdict(set)
        for prevCourse, nextCourse in relations:
            coursePrevCoursesMap[nextCourse].add(prevCourse)
            courseNextCoursesMap[prevCourse].add(nextCourse)

        currentSet = set()
        for i in range(1, n+1):
            if len(coursePrevCoursesMap[i]) == 0:
                coursePrevCoursesMap[i] = set()
                currentSet.add(i)
        
        taken = 0
        semesters = 0
        while len(currentSet) > 0:
            nextSet = set()
            for currentCourse in currentSet:
                for nextCourse in courseNextCoursesMap[currentCourse]:
                    coursePrevCoursesMap[nextCourse].remove(currentCourse)
                    if len(coursePrevCoursesMap[nextCourse]) == 0:
                        nextSet.add(nextCourse)
            taken += len(currentSet)
            semesters += 1
            currentSet = nextSet
        return semesters if taken == n else -1

# Unit Tests
import unittest
funcs = [Solution().minimumSemesters]
class TestMinimumSemesters(unittest.TestCase):
    def testMinimumSemesters1(self):
        for func in funcs:
            n = 3
            relations = [[1,3],[2,3]]
            self.assertEqual(func(n=n, relations=relations), 2)

    def testMinimumSemesters2(self):
        for func in funcs:
            n = 3
            relations = [[1,2],[2,3],[3,1]]
            self.assertEqual(func(n=n, relations=relations), -1)

if __name__ == "__main__":
    unittest.main()
