"""
362. Design Hit Counter
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:
- HitCounter() Initializes the object of the hit counter system.
- void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

Example1:
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.

Constraints:
1 <= timestamp <= 2 * 10^9
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.

Follow up: What if the number of hits per second could be huge? Does your design scale?
"""

"""
Note:
1. HashTable+Queue
Time:
    __init__: O(1)
    hit: O(1)
    getHits: O(1) amortized
Space: O(300)
"""

import collections
class HitCounter:

    # __init__ initializes the object of the hit counter system
    def __init__(self):
        self.largestSecondDifference = 300
        self.queue = collections.deque([])
        self.timestampHits = collections.defaultdict(int)
        self.hitCount = 0
    
    
    # hit records a hit that happened at timestamp (in seconds).
    # Several hits may happen at the same timestamp
    def hit(self, timestamp: int) -> None:
        self.timestampHits[timestamp] += 1
        self.hitCount += 1
        if self.timestampHits[timestamp] == 1:
            self.queue.append(timestamp)
        

    # getHits returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
    def getHits(self, timestamp: int) -> int:
        self._remove(timestamp)
        return self.hitCount
        
    
    def _remove(self, timestamp: int) -> None:
        while self.queue and (timestamp - self.queue[0] >= self.largestSecondDifference):
            self.hitCount -= self.timestampHits[self.queue[0]]
            del self.timestampHits[self.queue[0]]
            self.queue.popleft()

# Unit Tests
import unittest

classes = [HitCounter]
class TestHitCounter(unittest.TestCase):
    def testHitCounter1(self):
        for myclass in classes: 
            hitCounter = myclass()
            hitCounter.hit(1) # hit at timestamp 1.
            hitCounter.hit(2) # hit at timestamp 2.
            hitCounter.hit(3) # hit at timestamp 3.
            self.assertEqual(hitCounter.getHits(4), 3) # get hits at timestamp 4, return 3.
            hitCounter.hit(300) # hit at timestamp 300.
            self.assertEqual(hitCounter.getHits(300), 4) # get hits at timestamp 300, return 4.
            self.assertEqual(hitCounter.getHits(301), 3) # get hits at timestamp 301, return 3.

if __name__ == "__main__":
    unittest.main()
