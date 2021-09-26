"""
295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Design a data structure that supports the following two operations:
- void addNum(int num) - Add a integer number from the data stream to the data
- double findMedian() - Return the median of all elements so far.

Example1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""

"""
Note:
1. Two Heaps: O(logn) time | O(n) space
(1) min heap stores larger half of elements
(2) max heap stores smaller half of elements
(3) for addNum function
        make sure that every num in small is <= every num in large
        make sure that abs(len(self.small) - len(self.large)) <= 1

"""


import heapq
class MedianFinder:

    def __init__(self):
        self.small = []  # smaller half of elements, max heap
        self.large = []  # larger half of elements, min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every number in small is <= every number in large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            num = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            num = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * num)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2

# Unit Tests
import unittest

class TestMedianFinder(unittest.TestCase):
    def testMedianFinder(self):
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        medianFinder.addNum(2)
        self.assertEqual(medianFinder.findMedian(), 1.5)
        medianFinder.addNum(3)
        self.assertEqual(medianFinder.findMedian(), 2.0)


if __name__ == "__main__":
    unittest.main()
