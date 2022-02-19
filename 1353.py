"""
1353. Maximum Number of Events That Can Be Attended
You are given an array of events where events[i] = [startDay_i, endDay_i].
Every event i starts at startDay_i and ends at endDay_i.

You can attend an event i at any day d where startTime_i <= d <= endTime_i.
You can only attend one event at any time d.

Return the maximum number of events you can attend.

Example1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example2:
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Constraints:
1 <= events.length <= 10^5
events[i].length == 2
1 <= startDay_i <= endDay_i <= 10^5
"""

"""
Note:
1. Greedy Algorithm with minHeap: O(10^5 + nlogn) time | O(n) space
"""



from typing import List
import unittest, collections
import heapq

class Solution(object):
    def maxEvents(self, events: List[List[int]]) -> int:
        startDayEndDays = collections.defaultdict(list)
        lastEndDay = -1
        for startDay, endDay in events:
            startDayEndDays[startDay].append(endDay)
            lastEndDay = max(lastEndDay, endDay)
        
        count = 0
        minHeap = []
        for day in range(lastEndDay + 1):
            for endDay in startDayEndDays[day]:
                heapq.heappush(minHeap, endDay)
            
            while minHeap:
                endDay = heapq.heappop(minHeap)
                if endDay >= day:
                    count += 1
                    break
        return count


# Unit Tests
funcs = [Solution().maxEvents]


class TestMaxEvents(unittest.TestCase):
    def testMaxEvents1(self):
        for func in funcs:
            events = [[1,2],[2,3],[3,4]]
            self.assertEqual(func(events=events), 3)

    def testMaxEvents2(self):
        for func in funcs:
            events = [[1,2],[2,3],[3,4],[1,2]]
            self.assertEqual(func(events=events), 4)

    def testMaxEvents3(self):
        for func in funcs:
            events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
            self.assertEqual(func(events=events), 4)

    def testMaxEvents4(self):
        for func in funcs:
            events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
            self.assertEqual(func(events=events), 7)

    def testMaxEvents5(self):
        for func in funcs:
            events = [[1,2],[2,2],[3,3],[3,4],[3,4]]
            self.assertEqual(func(events=events), 4)

    def testMaxEvents6(self):
        for func in funcs:
            events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
            self.assertEqual(func(events=events), 5)


if __name__ == "__main__":
    unittest.main()
