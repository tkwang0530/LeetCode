"""
2211. Count Collisions on a Road
There are n cars on an infinitely long road. The cars are numbered from 0 to n-1 from left to right and each car is present at a unique point.

You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the i-th car is moving towards the left, the right, or staying at its current point respectively. Each moving car has the same speed.

The number of collisions can be calculated as follows:
- When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
- When a moving car collides with a stationary car, the number of collisions increases by 1.

After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.

Example1:
Input: directions = "RLRSLL"
Output: 5
Explanation:
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5. 

Example2:
Input: directions = "LLRR"
Output: 0
Explanation:
No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.

Constraints:
1 <= directions.length <= 10^5
directions[i] is either 'L', 'R', or 'S'.
"""

"""
Note:
1. Sliding Window: O(n) time | O(n) space - where n is the length of string directions
"""




import unittest
class Solution:
    def countCollisions(self, directions: str) -> int:
        if len(directions) <= 1:
            return 0

        count = 0
        directionChars = list(directions)
        for i in range(len(directionChars)-1):
            first, second = directionChars[i], directionChars[i+1]
            if first == "S" and second == "L":
                count += 1
                directionChars[i+1] = "S"
            elif first == "R" and second == "S":
                count += 1
                directionChars[i] = "S"
            elif first == "R" and second == "L":
                count += 2
                directionChars[i] = "S"
                directionChars[i+1] = "S"

        while directionChars and directionChars[-1] == "R":
            directionChars.pop()
        return count + directionChars.count("R")


# Unit Tests
funcs = [Solution().countCollisions]


class TestCountCollisions(unittest.TestCase):
    def testCountCollisions1(self):
        for func in funcs:
            directions = "RLRSLL"
            self.assertEqual(func(directions=directions), 5)

    def testCountCollisions2(self):
        for func in funcs:
            directions = "LLRR"
            self.assertEqual(func(directions=directions), 0)

    def testCountCollisions3(self):
        for func in funcs:
            directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
            self.assertEqual(func(directions=directions), 20)


if __name__ == "__main__":
    unittest.main()
