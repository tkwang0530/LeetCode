"""
621. Task Scheduler
description: https://leetcode.com/problems/task-scheduler/description/
"""

"""
Note:
1. Priority Queue: O(t + tlogm) time | O(m) space - where m is the number of unique tasks and t is the length of tasks
"""

import collections, heapq
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        intervalIdx = 0
        processingTasksMinHeap = [] # [[intervalIdx, Task, count]]
        readyTasksMaxHeap = [] # [(-count, Task)]
        counter = collections.Counter(tasks)

        idles = 0
        finished = 0
        for task, count in counter.items():
            nCount = -count
            heapq.heappush(readyTasksMaxHeap, [nCount, task])


        while finished < len(tasks):
            # update processingTasksMinHeap
            while processingTasksMinHeap and processingTasksMinHeap[0][0] <= intervalIdx:
                _, task, count = heapq.heappop(processingTasksMinHeap)
                heapq.heappush(readyTasksMaxHeap, [-count, task])
            if not readyTasksMaxHeap:
                newIntervalIdx, task, count = heapq.heappop(processingTasksMinHeap)
                heapq.heappush(readyTasksMaxHeap, [-count, task])
                idles += newIntervalIdx-intervalIdx
                intervalIdx = newIntervalIdx

            nCount, task = heapq.heappop(readyTasksMaxHeap)
            finished += 1
            count = -nCount-1
            if count > 0:
                heapq.heappush(processingTasksMinHeap, [intervalIdx+n+1, task, count])
            intervalIdx += 1

        return idles + len(tasks)

# Unit Tests
import unittest
funcs = [Solution().leastInterval]

class TestLeastInterval(unittest.TestCase):
    def testLeastInterval1(self):
        for func in funcs:
            tasks = ["A","A","A","B","B","B"]
            n = 2
            self.assertEqual(func(tasks=tasks, n=n), 8)

    def testLeastInterval2(self):
        for func in funcs:
            tasks = ["A","C","A","B","D","B"]
            n = 1
            self.assertEqual(func(tasks=tasks, n=n), 6)

    def testLeastInterval3(self):
        for func in funcs:
            tasks = ["A","A","A", "B","B","B"]
            n = 3
            self.assertEqual(func(tasks=tasks, n=n), 10)

if __name__ == "__main__":
    unittest.main()