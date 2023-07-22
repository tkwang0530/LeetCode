"""
731. My Calendar II
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Example1:
Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

Constraints:
0 <= start < end <= 10^9
At most 1000 calls will be made to book.
"""

"""
Note:
1. Sweep Line:
__init__: O(1) time | O(1) space
book: O(nlogn) time | O(n) space - where n is the number of timestamp
total space: O(n) space - where n is the number of timestamp

2. Interval overlap check:
__init__: O(1) time | O(1) space
book: O(n) time | O(1) space - where n is the number of book
total space: O(n) space - where n is the number of book

We store an array self.overlaps of intervals that are double booked, and self.calendar for intervals which have been single booked.
use the logic (start < j and end > i) to check if the ranges [start, end) and [i, j) overlap.

The clever idea is we do not need to "clean up" ranges in calendar; if we have [1, 3] and [2, 4], this will be calendar = [[1, 3], [2, 4]] and overlaps = [[2, 3]]. We don't need to spend time transforming the calendar to calendar = [[1, 4]]
"""

import unittest
import collections
class MyCalendarTwo:

    def __init__(self):
        self.sweep = collections.defaultdict(int)


    def book(self, start: int, end: int) -> bool:
        self.sweep[start] += 1
        self.sweep[end] -= 1
        bookings = 0
        for time in sorted(self.sweep.keys()):
            bookings += self.sweep[time]
            if bookings >= 3:
                self.sweep[start] -= 1
                self.sweep[end] += 1
                return False
        return True

class MyCalendarTwo2:

    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for oStart, oEnd in self.overlaps:
            if start < oEnd and end > oStart:
                return False
            
        for cStart, cEnd in self.calendar:
            if start < cEnd and end > cStart:
                self.overlaps.append((max(start, cStart), min(end, cEnd)))
        self.calendar.append((start, end))
        return True
# Unit Tests
classes = [MyCalendarTwo, MyCalendarTwo2]


class TestMyCalendarTwo(unittest.TestCase):
    def testMyCalendarTwo1(self):
        for myclass in classes:
            myCalendarTwo = myclass()
            self.assertEqual(myCalendarTwo.book(10, 20), True)
            self.assertEqual(myCalendarTwo.book(50, 60), True)

            self.assertEqual(myCalendarTwo.book(10, 40), True)
            self.assertEqual(myCalendarTwo.book(5, 15), False)
            self.assertEqual(myCalendarTwo.book(5, 10), True)
            self.assertEqual(myCalendarTwo.book(25, 55), True)


if __name__ == "__main__":
    unittest.main()
