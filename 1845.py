"""
1845. Seat Reservation Manager
description: https://leetcode.com/problems/seat-reservation-manager/description/
"""

"""
Note:
1. PriorityQueue + HashSet:
reserve() -> O(logn) time | O(n) space
unreserve() -> O(logn)
"""

import unittest, heapq
class SeatManager:

    def __init__(self, n: int):
        self.reserved = set()
        self.availables = [i+1 for i in range(n)]

    # Fetches the smallest-numbered unreserved seat, reserves it, and returns its number
    def reserve(self) -> int:
        number = heapq.heappop(self.availables)
        self.reserved.add(number)
        return number
        
    # Unreserves the seat with the given seatNumber
    def unreserve(self, seatNumber: int) -> None:
        self.reserved.remove(seatNumber)
        heapq.heappush(self.availables, seatNumber)


# Unit Tests
classes = [SeatManager]

class TestSeatManager(unittest.TestCase):
    def testSeatManager1(self):
        for myclass in classes:
            seatManager = SeatManager(5)
            self.assertEqual(seatManager.reserve(), 1)
            self.assertEqual(seatManager.reserve(), 2)

            seatManager.unreserve(2)
            self.assertEqual(seatManager.reserve(), 2)

            self.assertEqual(seatManager.reserve(), 3)
            self.assertEqual(seatManager.reserve(), 4)
            self.assertEqual(seatManager.reserve(), 5)
            seatManager.unreserve(5)
        


if __name__ == "__main__":
    unittest.main()
