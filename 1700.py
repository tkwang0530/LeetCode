"""
1700. Number of Students Unable to Eat Lunch
description: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
"""

"""
Note:
1. Simulation: O(n^2) time | O(2n) space - where n is the length of the array students
2. HashMap: O(n) time | O(2) space - where n is the length of the array students
"""

from typing import List
import unittest, collections
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        queue = collections.deque(students)
        sandwiches.reverse()

        rounds = 0
        while queue and rounds <= n**2:
            preferLabel = queue.popleft()
            if preferLabel == sandwiches[-1]:
                sandwiches.pop()
            else:
                queue.append(preferLabel)
            rounds += 1
        
        return len(queue)
    
class Solution2:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        counter = collections.Counter(students)
        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                counter[sandwich] -= 1
            else:
                break
        return sum(counter.values())

    
# Unit Tests
funcs = [Solution().countStudents, Solution2().countStudents]


class TestCountStudents(unittest.TestCase):
    def testCountStudents1(self):
        for func in funcs:
            students = [1,1,0,0]
            sandwiches = [0,1,0,1]
            self.assertEqual(func(students=students, sandwiches=sandwiches), 0)

    def testCountStudents2(self):
        for func in funcs:
            students = [1,1,1,0,0,1]
            sandwiches = [1,0,0,0,1,1]
            self.assertEqual(func(students=students, sandwiches=sandwiches), 3)

if __name__ == "__main__":
    unittest.main()