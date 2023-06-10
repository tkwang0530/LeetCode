"""
2013. Detect Squares
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.


Example1:
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points

Constraints:
point.length == 2
0 <= x, y <= 1000
At most 3000 calls in total will be made to add and count.
"""

"""
Note:
1. HashMap: 
__init__: O(1) time | O(1) space
add: O(1) time | O(1) space
count: O(n) time | O(1) space
where n is the range of x, that is 1000-0+1 = 1001
"""

import unittest, collections
from typing import List
# Author: Tommy
class DetectSquares:

    # __init__ initializes the object with an empty data structure
    def __init__(self):
        self.pointPerY = collections.defaultdict(collections.Counter)

    # add adds a new point (point=[x, y]) to the data structure
    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointPerY[y][x] += 1
        

    # count counts the number of ways to form axis-aligned squares with point (point=[x, y]) as described above.
    def count(self, point: List[int]) -> int:
        x1,y1 = point
        xCount = self.pointPerY[y1]
        output = 0
        for x2 in self.pointPerY[y1]:
            if x1 == x2:
                continue
            y2 = y1
            count2 = self.pointPerY[y2][x2]
            for y3 in [(y1-abs(x1-x2)), (y1+abs(x2-x1))]:
                x3 = x1
                count3 = self.pointPerY[y3][x3]

                y4 = y3
                x4 = x2
                count4 = self.pointPerY[y4][x4]
                output += count2 * count3 * count4
        return output

# Unit Tests
import unittest
classes = [DetectSquares]
class TestDetectSquares(unittest.TestCase):
    def testDetectSquares1(self):
        for myclass in classes:
            detectSquares = myclass()
            detectSquares.add([3, 10])
            detectSquares.add([11, 2])
            detectSquares.add([3, 2])

            # return 1. You can choose: The first, second, and third points
            self.assertEqual(detectSquares.count([11, 10]), 1) 

            # return 0. The query point cannot form a square with any points in the data structure.
            self.assertEqual(detectSquares.count([14, 8]), 0)

            # Adding duplicate points is allowed
            detectSquares.add([11, 2])

            # return 2. You can choose: 
            # - The first, second, and third points
            # - The first, third, and fourth points
            self.assertEqual(detectSquares.count([11, 10]), 2) 

if __name__ == "__main__":
    unittest.main()
