"""
2037. Minimum Number of Moves to Seat Everyone
description: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
"""

"""
Note:
1. Sort + Greedy: O(nlogn) time | O(sort) space - where n is the length of the array seats
"""


from typing import List
import unittest
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i]-students[i])
        return moves

# Unit Tests
funcs = [Solution().minMovesToSeat]
class TestMinMovesToSeat(unittest.TestCase):
    def testMinMovesToSeat1(self):
        for minMovesToSeat in funcs:
            seats = [3,1,5]
            students = [2,7,4]
            self.assertEqual(minMovesToSeat(seats=seats, students=students), 4)

    def testMinMovesToSeat2(self):
        for minMovesToSeat in funcs:
            seats = [4,1,5,9]
            students = [1,3,2,6]
            self.assertEqual(minMovesToSeat(seats=seats, students=students), 7)

    def testMinMovesToSeat3(self):
        for minMovesToSeat in funcs:
            seats = [2,2,6,6]
            students = [1,3,2,6]
            self.assertEqual(minMovesToSeat(seats=seats, students=students), 4)

if __name__ == "__main__":
    unittest.main()
