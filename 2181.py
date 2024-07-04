"""
2181. Merge Nodes in Between Zeros
description: https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
"""

"""
Note:
1. One pass: O(n) time | O(n) space - where n is the length of the linked list
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = dummy = ListNode(0)
        current = head.next
        runningSum = 0
        while current:
            if current.val > 0:
                runningSum += current.val
            else:
                ptr.next = ListNode(runningSum)
                ptr = ptr.next
                runningSum = 0
            current = current.next
        return dummy.next

def listToStr(head: Optional[ListNode]) -> str:
    output = []
    current = head
    while current:
        output.append(str(current.val))
        current = current.next

    output.append("None")
    return "->".join(output)

# Unit Tests
import unittest
funcs = [Solution().mergeNodes]

class TestMergeNodes(unittest.TestCase):
    def testMergeNodes1(self):
        for mergeNodes in funcs:
            head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
            self.assertEqual(listToStr(mergeNodes(head=head)), "4->11->None")

    def testMergeNodes2(self):
        for mergeNodes in funcs:
            head = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
            self.assertEqual(listToStr(mergeNodes(head=head)), "1->3->4->None")

if __name__ == "__main__":
    unittest.main()