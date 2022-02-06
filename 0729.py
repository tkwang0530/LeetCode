"""
729. My Calendar I
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:
- MyCalendar() Initializes the calendar object.
- boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example1:
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

Constraints:
0 <= start < end <= 10^9
At most 1000 calls will be made to book.
"""

"""
Note:
1. Segment Tree: O(logn) time | O(n) time
"""
class TreeNode:
    def __init__(self, left: int, right: int) -> None:
        self.left = None
        self.right = None
        self.range = (left, right) # [left, right)
        self.booked = False

class MyCalendar:

    def __init__(self):
        self.root = TreeNode(0, 10 ** 9 + 1)

    def update(self, root, left, right):
        if left <= root.range[0] and right >= root.range[1]:
            root.booked = True
            return
        
        mid = root.range[0] + (root.range[1] - root.range[0]) // 2

        if left < mid:
            if not root.left:
                root.left = TreeNode(root.range[0], mid)
            self.update(root.left, left, right)

        if right > mid:
            if not root.right:
                root.right = TreeNode(mid, root.range[1])
            self.update(root.right, left, right)

    def query(self, root, left, right):
        if root.booked:
            return True
        
        mid = root.range[0] + (root.range[1] - root.range[0]) // 2
        if left < mid and root.left and self.query(root.left, left , right):
            return True
        
        if right > mid and root.right and self.query(root.right, left, right):
            return True
        
        return False

    def book(self, start: int, end: int) -> bool:
        if not self.query(self.root, start, end):
            self.update(self.root, start, end)
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# Unit Tests
import unittest

class TestMyCalendar(unittest.TestCase):
    def testMyCalendar1(self):
        myCalendar = MyCalendar()
        self.assertEqual(myCalendar.book(10, 20), True)
        self.assertEqual(myCalendar.book(15, 25), False)
        self.assertEqual(myCalendar.book(20, 30), True)

if __name__ == "__main__":
    unittest.main()