"""
735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroid meet, the smaller one will explode. if both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

"""
Note:
1. Stack: O(n) time | O(n) space
"""

from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = []
        right = []
        for asteroid in asteroids:
            if asteroid > 0:
                right.append(asteroid)
                continue
            
            while right and right[-1] < abs(asteroid):
                right.pop()
            
            if right and right[-1] == abs(asteroid):
                right.pop()
            elif not right:
                left.append(asteroid)
        left.extend(right)
        return left

# Unit Tests
import unittest
funcs = [Solution().asteroidCollision]
class TestAsteroidCollision(unittest.TestCase):
    def testAsteroidCollision1(self):
        for func in funcs:
            asteroids = [5,10,-5]
            self.assertEqual(func(asteroids=asteroids), [5,10])

    def testAsteroidCollision2(self):
        for func in funcs:
            asteroids = [8,-8]
            self.assertEqual(func(asteroids=asteroids), [])

    def testAsteroidCollision3(self):
        for func in funcs:
            asteroids = [10,2,-5]
            self.assertEqual(func(asteroids=asteroids), [10])

if __name__ == "__main__":
    unittest.main()
