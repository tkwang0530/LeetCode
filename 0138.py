"""
138. Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Contruct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list representthe same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
- val: an integer representing Node.val
- random_index: the index of node (range from 0 to n - 1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example4:
Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.

Constraints:
0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random is null or is pointing to some node in the linked list.
"""

"""
Note:
1. Hash Table + Two Pass: O(n) time | O(n) space
(1) first pass: copy linked list with only val + map original node to new node <originalNode, newNode>
(2) second pass: setting the random and next properties of each node
"""

import unittest
class Node:
    def __init__(self, val=0, next=None, random=None) -> None:
        self.val = val
        self.next = next
        self.random = random

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
    def copyRandomList(self, head: Node) -> Node:
        oldToCopy = { None : None}
        current = head
        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current = current.next
        return oldToCopy[head]

# Unit Tests
funcs = [Solution().copyRandomList]


class TestCopyRandomList(unittest.TestCase):
    def testCopyRandomList1(self):
        for func in funcs:
            head = Node.fromArray([7,13,11,10,1])
            node7 = head
            node13 = node7.next
            node11 = node13.next
            node10 = node11.next
            node1 = node10.next

            node13.random = node7
            node11.random = node1
            node10.random = node11
            node1.random = node7

            copyHead = func(head=head)
            self.assertEqual(repr(copyHead), "7->13->11->10->1->None")
            copyNode7 = copyHead
            copyNode13 = copyNode7.next
            copyNode11 = copyNode13.next
            copyNode10 = copyNode11.next
            copyNode1 = copyNode10.next
            self.assertEqual(copyNode7.random, None)
            self.assertEqual(id(copyNode13.random), id(copyNode7))
            self.assertEqual(id(copyNode11.random), id(copyNode1))
            self.assertEqual(id(copyNode10.random), id(copyNode11))
            self.assertEqual(id(copyNode1.random), id(copyNode7))


if __name__ == "__main__":
    unittest.main()
