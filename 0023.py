"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example2:
Input: lists = []
Output: []

Example3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""

"""
Note:
1. Brute Force: O(nk) time | O(1) space - where n is the total number of nodes
Merge two linked list (extend) - where n is the total number of nodes
2. Merge sort: O(nlogk) time | O(logk) space - where n is the total number of nodes
3. Use Heap: O(nlogk) time | O(k) space - where n is the total number of nodes

Extra:
heapreplace(a, x) returns the smallest value originally in a regardless of the value of x
heappushpop(a, x) pushes x onto a before popping the smallest value
"""

from typing import Optional, List
from heapq import heapify, heappop, heapreplace
import unittest
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    # TEST ONLY
    def __repr__(self):
        return f"{self.val}->{self.next}"

    @classmethod
    def fromArray(cls, arr):
        if arr is None:
            return None
        idx = 0
        length = len(arr)
        dummy = cls(0)
        current = dummy
        while idx < length:
            current.next = cls(arr[idx])
            current = current.next
            idx += 1
        return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        dummy = prev = ListNode(0)
        while True:
            minNode = None
            minIdx = -1
            for i, list in enumerate(lists):
                if not list:
                    continue
                if not minNode or list.val < minNode.val:
                    minNode = list
                    minIdx = i
            if not minNode:
                break

            prev.next = minNode
            prev = prev.next

            lists[minIdx] = minNode.next
        return dummy.next

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            current = dummy = ListNode(0)
            while l1 or l2:
                val1 = l1.val if l1 else float("inf")
                val2 = l2.val if l2 else float("inf")
                if val1 < val2:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            return dummy.next

        def mergeKListsHelper(start: int, end: int) -> Optional[ListNode]:
            if end < start:
                return None
            if start == end:
                return lists[start]
            
            mid = start + (end - start) // 2
            left = mergeKListsHelper(start, mid)
            right = mergeKListsHelper(mid+1, end)
            return mergeTwoLists(left, right)

        return mergeKListsHelper(0, len(lists)-1)
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return dummy.next
    
    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(minHeap)
        dummy = curr = ListNode(0)
        while len(minHeap) > 0:
            val, i, node = minHeap[0]
            if not node.next:
                heappop(minHeap)
            else:
                heapreplace(minHeap, (node.next.val, i, node.next))
            curr.next = node
            curr = curr.next
        return dummy.next




# Unit Tests
funcs = [Solution().mergeKLists, Solution().mergeKLists2, Solution().mergeKLists3]


class TestMergeKLists(unittest.TestCase):
    def testMergeKLists1(self):
        for func in funcs:
            lists = [ListNode.fromArray([1, 4, 5]),ListNode.fromArray([1, 3, 4]),ListNode.fromArray([2, 6])]
            self.assertEqual(repr(func(lists=lists)), "1->1->2->3->4->4->5->6->None")

    def testMergeKLists2(self):
        for func in funcs:
            lists = []
            self.assertEqual(repr(func(lists=lists)), "None")

    def testMergeKLists3(self):
        for func in funcs:
            lists = [None]
            self.assertEqual(repr(func(lists=lists)), "None")


if __name__ == "__main__":
    unittest.main()
