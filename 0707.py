"""
707. Design Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked lists are 0-indexed.

Implement the MyLinkedList class:
- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index-th node in the linked list. if the index is invalid, return -1
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the index-th node int the linked list. if index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the index-th node in the linked list, if the index is valid.

Example1:
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""

import unittest
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

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


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummyHead = ListNode(0)
        self.dummyTail = ListNode(0)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead
        self.length = 0
        
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        node = self.dummyHead.next
        while index > 0:
            index -= 1
            node = node.next
        return node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        next = self.dummyHead.next
        newNode = ListNode(val, next, self.dummyHead)
        self.dummyHead.next = next.prev = newNode
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        prev = self.dummyTail.prev
        newNode = ListNode(val, self.dummyTail, prev)
        prev.next = self.dummyTail.prev = newNode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.length:
            self.addAtTail(val)
            return
        
        if index < 0 or index > self.length:
            return
            
        node = self.dummyHead.next
        while index > 0:
            index -= 1
            node = node.next
        prev = node.prev
        newNode = ListNode(val, node, prev)
        prev.next = node.prev = newNode
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return
        
        node = self.dummyHead.next
        while index > 0:
            index -= 1
            node = node.next
        self.removeNode(node)
        self.length -= 1
        
        
        
    def removeNode(self, node: ListNode) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = node.prev = None

# Unit Tests
classes = [MyLinkedList]

class TestMyLinkedList(unittest.TestCase):
    def testMyLinkedList1(self):
        for MyLinkedList in classes:
            myLinkedList = MyLinkedList()
            myLinkedList.addAtHead(1)
            myLinkedList.addAtTail(3)
            myLinkedList.addAtIndex(1, 2)
            self.assertEqual(repr(myLinkedList.dummyHead.next), "1->2->3->0->None")
            self.assertEqual(myLinkedList.get(1), 2)
            myLinkedList.deleteAtIndex(1)
            self.assertEqual(repr(myLinkedList.dummyHead.next), "1->3->0->None")
            self.assertEqual(myLinkedList.get(1), 3)


if __name__ == "__main__":
    unittest.main()
