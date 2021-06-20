"""
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Examples:
    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1
    m.next(10) = (1 + 10) / 2
    m.next(3) = (1 + 10 + 3) / 3
    m.next(5) = (10 + 3 + 5) / 3
"""

"""
Note:
Using a queue (Python deque)
O(1) time | O(n) space
"""

from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val):
        if len(self.queue) == self.size:
            temp = self.queue.popleft()
            self.total -= temp
        self.queue.append(val)
        self.total += val
        return self.total / len(self.queue)


# Unit Tests
import unittest


class TestMovingAverage(unittest.TestCase):
    def testMovingAverage1(self):
        m = MovingAverage(3)
        self.assertEqual(m.next(1), 1)
        self.assertEqual(m.next(10), 11 / 2)
        self.assertEqual(m.next(3), 14 / 3)
        self.assertEqual(m.next(5), 18 / 3)


if __name__ == "__main__":
    unittest.main()