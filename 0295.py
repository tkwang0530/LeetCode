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
min heap stores larger half of elements
max heap stores smaller half of elements

invariance:
(1) even # of elements: len(small), len(large) = (k, k)
(2) odd # of elements: len(small), len(large) = (k, k+1)
after adding a #:
(1) len(small), len(large) = (k, k + 1)
(2) len(small), len(large) = (k+1, k+1)

case1 (k, k) -> (k, k+1): push element to small, pop one element out of small, and push to large
case2 (k, k+1) -> (k+1, k+1): push element to large, pop one element out of large, and push to small
"""




import unittest
from heapq import *
class MedianFinder:

    def __init__(self):
        self.small = []  # smaller half of elements, max heap
        self.large = []  # larger half of elements, min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):  # case1 (k, k)
            heappush(self.large, -heappushpop(self.small, -num))
        else:  # case2 (k, k+1)
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):  # (k, k)
            return (self.large[0] - self.small[0]) / 2
        else:  # (k, k+1)
            return self.large[0]

# Unit Tests


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
