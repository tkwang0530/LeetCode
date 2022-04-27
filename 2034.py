"""
2034. Stock Price Fluctuation
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:
- Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
- Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
- Finds the maximum price the stock has been based on the current records.
- Finds the minimum price the stock has been based on the current records.

Implement the StockPrice class:
- StockPrice() Initializes the object with no price records.
- void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
- int current() Returns the latest price of the stock.
- int maximum() Returns the maximum price of the stock.
- int minimum() Returns the minimum price of the stock.

Example1:
Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.

Constraints:
1 <= timestamp, price <= 10^9
At most 10^5 calls will be made in total to update, current, maximum, and minimum.
current, maximum, and minimum will be called only after update has been called at least once.
"""

"""
Note:
1. Two Heaps:
Total Space Complexity: O(n)
__init__: O(1) time
update: O(logn) time
current: O(1) time
maximum: O(logn) time (average)
minimum: O(logn) time (average)

2. Binary Search Tree (SortedDict)
Total Space Complexity: O(n)
__init__: O(1) time
update: O(logn) time
current: O(1ogn) time
maximum: O(logn) time
minimum: O(logn) time
"""

import unittest, heapq
class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.highestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        # keep track of current prices
        self.timestamps[timestamp] = price
        self.highestTimestamp = max(self.highestTimestamp, timestamp)

        # for maximum/minimum
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.highestTimestamp]

    def maximum(self) -> int:
        currentPrice, timestamp = heapq.heappop(self.maxHeap)

        while -currentPrice != self.timestamps[timestamp]:
            currentPrice, timestamp = heapq.heappop(self.maxHeap)
        
        heapq.heappush(self.maxHeap, (currentPrice, timestamp))
        return -currentPrice

    def minimum(self) -> int:
        currentPrice, timestamp = heapq.heappop(self.minHeap)

        while currentPrice != self.timestamps[timestamp]:
            currentPrice, timestamp = heapq.heappop(self.minHeap)
        
        heapq.heappush(self.minHeap, (currentPrice, timestamp))
        return currentPrice

from sortedcontainers import SortedDict
class StockPrice2:

    def __init__(self):
        self.timestamps = SortedDict()
        self.records = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timestamps:
            previousPrice = self.timestamps[timestamp]
            self.records[previousPrice].remove(timestamp)
            if len(self.records[previousPrice]) == 0:
                self.records.pop(previousPrice)
        if price not in self.records:
            self.records[price] = set()
        self.records[price].add(timestamp)
        self.timestamps[timestamp] = price

    def current(self) -> int:
        return self.timestamps.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.records.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.records.peekitem(0)[0]

# Unit Tests
classes = [StockPrice, StockPrice2]

class TestLRUCache(unittest.TestCase):
    def testLRUCache1(self):
        for myclass in classes:
            stockPrice = myclass()
            stockPrice.update(1, 10) # Timestamps are [1] with corresponding prices [10].
            stockPrice.update(2, 5) # Timestamps are [1, 2] with corresponding prices [10, 5].
            
            self.assertEqual(stockPrice.current(), 5) # return 5, the latest timestamp is 2 with the price being 5.

            self.assertEqual(stockPrice.maximum(), 10) # return 10, the maximum price is 10 at timestamp 1.

            stockPrice.update(1, 3) # The previous timestamp 1 had the wrong price, so it is updated to 3.
            # Timestamps are [1,2] with corresponding prices [3,5].

            self.assertEqual(stockPrice.maximum(), 5) # return 5, the maximum price is 5 after the correction.

            stockPrice.update(4, 2) # Timestamps are [1,2,4] with corresponding prices [3,5,2].
            self.assertEqual(stockPrice.minimum(), 2) # return 2, the minimum price is 2 at timestamp 4.

if __name__ == "__main__":
    unittest.main()
