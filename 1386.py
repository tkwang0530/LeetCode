"""
1386. Cinema Seat Allocation
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

Example1:
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.

Example2:
Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2

Example3:
Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4

Constraints:
1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
All reservedSeats[i] are distinct.
"""

"""
Note:
1. HashTable + Bucket Concept: O(m) time | O(1) space - where m is the number of reservedSeats
"""

from typing import List
import collections
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        group1 = {2, 3, 4, 5}
        group2 = {4, 5, 6, 7}
        group3 = {6, 7, 8, 9}
        res = (n * 2)
        rowAvailables = collections.defaultdict(list)
        for row, col in reservedSeats:
            if row not in rowAvailables:
                rowAvailables[row] = [1, 1, 1]
            if col in group1:
                rowAvailables[row][0] = 0
            if col in group2:
                rowAvailables[row][1] = 0
            if col in group3:
                rowAvailables[row][2] = 0
        for row, available in rowAvailables.items():
            availableCount = 0
            if available[0] == 1 and available[2] == 1:
                availableCount = 2
            elif sum(available) > 0:
                availableCount = 1
            res -= (2 - availableCount)
        return res

# Unit Tests
import unittest
funcs = [Solution().maxNumberOfFamilies]
class TestMaxNumberOfFamilies(unittest.TestCase):
    def testMaxNumberOfFamilies1(self):
        for func in funcs:
            n = 3
            reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
            self.assertEqual(func(n=n, reservedSeats=reservedSeats), 4)

    def testMaxNumberOfFamilies2(self):
        for func in funcs:
            n = 2
            reservedSeats = [[2,1],[1,8],[2,6]]
            self.assertEqual(func(n=n, reservedSeats=reservedSeats), 2)

    def testMaxNumberOfFamilies3(self):
        for func in funcs:
            n = 4
            reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
            self.assertEqual(func(n=n, reservedSeats=reservedSeats), 4)

if __name__ == "__main__":
    unittest.main()
