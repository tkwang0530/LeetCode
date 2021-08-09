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

"""
Note:
1. 
"""




import unittest
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    # TEST ONLY
    def __repr__(self):
        nums = [self.val]
        while self.next:
            nums.append(self.next.val)
            self = self.next
        return "->".join(str(num) for num in nums)

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
        self.length = 0
        self.dummy = ListNode(0)
    
    def get(self, index: int):
        if index < 0 or index > self.length -1 :
            return -1
        curr = self.dummy.next
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.val
    
    def addAtHead(self, val: int):
        newNode = ListNode(val)
        newNode.next = self.dummy.next
        self.dummy.next = newNode
        self.length += 1

    def addAtTail(self, val: int):
        newNode = ListNode(val)
        curr = self.dummy
        for _ in range(self.length):
            curr = curr.next
        curr.next = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int):
        if index < 0 or index > self.length:
            return

        newNode = ListNode(val)
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode
        self.length += 1
    
    def deleteAtIndex(self, index: int):
        if index < 0 or index > self.length - 1:
            return
        curr = self.dummy
        while index > 0:
            curr = curr.next
            index -= 1
        curr.next = curr.next.next
        self.length -= 1
        

# Unit Tests
classes = [MyLinkedList]

class TestMyLinkedList(unittest.TestCase):
    def testMyLinkedList1(self):
        for MyLinkedList in classes:
            myLinkedList = MyLinkedList()
            myLinkedList.addAtHead(1)
            myLinkedList.addAtTail(3)
            myLinkedList.addAtIndex(1, 2)
            self.assertEqual(repr(myLinkedList.dummy.next), "1->2->3")
            self.assertEqual(myLinkedList.get(1), 2)
            myLinkedList.deleteAtIndex(1)
            self.assertEqual(repr(myLinkedList.dummy.next), "1->3")
            self.assertEqual(myLinkedList.get(1), 3)


if __name__ == "__main__":
    unittest.main()
