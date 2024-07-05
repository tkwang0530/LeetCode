"""
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
description: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/
"""

"""
Note:
1. One pass: O(n) time | O(1) space - where n is the length of the linked list
"""

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        maxCP = -float("inf")
        minCP = float("inf")
        CPs = 0
        current = head.next
        prev = head
        
        def isLocalMax(prev, current):
            return current.val > prev.val and current.val > current.next.val

        def isLocalMin(prev, current):
            return current.val < prev.val and current.val < current.next.val

        firstCPIdx = -1
        lastCPIdx = -1
        idx = 1
        minDiff = float("inf")
        CPs = 0
        while current.next:
            if isLocalMax(prev, current) or isLocalMin(prev, current):
                CPs += 1
                if firstCPIdx < 0:
                    firstCPIdx = idx
                if CPs > 1:
                    minDiff = min(minDiff, idx-lastCPIdx)

                lastCPIdx = idx
            prev, current = current, current.next
            idx += 1

        if CPs < 2:
            return [-1, -1]

        return [minDiff, lastCPIdx-firstCPIdx]

# Unit Tests
import unittest
funcs = [Solution().nodesBetweenCriticalPoints]

class TestNodesBetweenCriticalPoints(unittest.TestCase):
    def nodesBetweenCriticalPoints(self):
        for nodesBetweenCriticalPoints in funcs:
            head = ListNode(3, ListNode(1))
            self.assertEqual(nodesBetweenCriticalPoints(head=head), [-1, -1])

    def testNodesBetweenCriticalPoints2(self):
        for nodesBetweenCriticalPoints in funcs:
            head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
            self.assertEqual(nodesBetweenCriticalPoints(head=head), [1, 3])

    def testNodesBetweenCriticalPoints3(self):
        for nodesBetweenCriticalPoints in funcs:
            head = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))))))
            self.assertEqual(nodesBetweenCriticalPoints(head=head), [3,3])

if __name__ == "__main__":
    unittest.main()