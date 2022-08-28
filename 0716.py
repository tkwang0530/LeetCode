"""
716. Max Stack
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:
- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Example1:
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
"""

"""
Note:
1. HashTable+LinkedList+maxHeap
# Average Time  : push -> O(1), pop -> O(1), top -> O(1), peekMax -> O(logm), popMax -> O(logm)
# Average Space : push -> O(1), pop -> O(1), top -> O(1), peekMax -> O(1), popMax -> O(1)
where m is the unique number count in the stack

2. HashTable+LinkedList+BST
Time: 
- push: O(logm)
- pop: O(logm)
- top: O(1)
- peekMax: O(1)
- popMax: O(logm)
Space: O(1)
where m is the unique number count in the stack
"""

import heapq, collections
class TreeNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MaxStack:

    # Initialize the stack object
    def __init__(self):
        self.dummyHead = TreeNode(0)
        self.dummyTail = TreeNode(0)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead
        self.numStack = collections.defaultdict(list)
        self.maxHeap = []
    
    # _insertNodeToHead insert a new node with value (val) to the head of the doubly linkedlist
    def _insertNodeToHead(self, val) -> None:
        prev, next = self.dummyHead, self.dummyHead.next
        newNode = TreeNode(val, prev, next)
        prev.next = next.prev = newNode
    
    # _removeNode removes specific node from the double linkedlist
    def _removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    # Pushes element x onto the stack
    def push(self, x: int) -> None:
        self._insertNodeToHead(x)
        self.numStack[x].append(self.dummyHead.next)
        if len(self.numStack[x]) == 1:
            heapq.heappush(self.maxHeap, -1 * x)

    # Removes the element on top of the stack and returns it
    def pop(self) -> int:
        topVal = self.top()
        self._removeK(topVal)
        return topVal
        
    
    # Gets the element on the top of the stack without removing it
    def top(self) -> int:
        return self.dummyHead.next.val
    
    # _removeK removes the toppest element with value k
    def _removeK(self, k) -> None:
        node = self.numStack[k].pop()
        self._removeNode(node)
        # TODO: maintain the maxHeap, remove the number will zero count
            
    
    # Retrieves the maximum element in the stack without removing it
    def peekMax(self) -> int:
        while self.maxHeap and len(self.numStack[-1*self.maxHeap[0]]) == 0:
            del self.numStack[-1*self.maxHeap[0]]
            heapq.heappop(self.maxHeap)
        return -1*self.maxHeap[0]
        
    # Retrieves the maximum element in the stack and removes it. If there if more than one maximum element, only remove the top-most one.
    def popMax(self) -> int:
        maxVal = self.peekMax()
        self._removeK(maxVal)
        return maxVal

from sortedcontainers import SortedList
class MaxStack2:

    # Initialize the stack object
    def __init__(self):
        self.dummyHead = TreeNode(0)
        self.dummyTail = TreeNode(0)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead
        self.numStack = collections.defaultdict(list)
        self.sortedList = SortedList()
    # _insertNodeToHead insert a new node with value (val) to the head of the doubly linkedlist
    def _insertNodeToHead(self, val) -> None:
        prev, next = self.dummyHead, self.dummyHead.next
        newNode = TreeNode(val, prev, next)
        prev.next = next.prev = newNode
    
    # _removeNode removes specific node from the double linkedlist
    def _removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    # Pushes element x onto the stack
    def push(self, x: int) -> None:
        self._insertNodeToHead(x)
        self.numStack[x].append(self.dummyHead.next)
        if len(self.numStack[x]) == 1:
            self.sortedList.add(x)

    # Removes the element on top of the stack and returns it
    def pop(self) -> int:
        topVal = self.top()
        self._removeK(topVal)
        return topVal
        
    
    # Gets the element on the top of the stack without removing it
    def top(self) -> int:
        return self.dummyHead.next.val
    
    # _removeK removes the toppest element with value k
    def _removeK(self, k) -> None:
        node = self.numStack[k].pop()
        self._removeNode(node)
        if not self.numStack[k]:
            del self.numStack[k]
            self.sortedList.remove(k)
    
    # Retrieves the maximum element in the stack without removing it
    def peekMax(self) -> int:
        return self.sortedList[-1]
        
    # Retrieves the maximum element in the stack and removes it. If there if more than one maximum element, only remove the top-most one.
    def popMax(self) -> int:
        maxVal = self.peekMax()
        self._removeK(maxVal)
        return maxVal
# Unit Tests
import unittest

classes = [MaxStack, MaxStack2]
class TestMaxStack(unittest.TestCase):
    def testMaxStack1(self):
        for myclass in classes: 
            stk = myclass()
            stk.push(5) # [5] the top of the stack and the maximum number is 5.
            stk.push(1) # [5, 1] the top of the stack is 1, but the maximum is 5.
            stk.push(5) # [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.

            self.assertEqual(stk.top(), 5) # return 5, [5, 1, 5] the stack did not change.
            self.assertEqual(stk.popMax(), 5) # return 5, [5, 1] the stack is changed now, and the top is different from the max.
            self.assertEqual(stk.top(), 1) # return 1, [5, 1] the stack did not change.
            self.assertEqual(stk.peekMax(), 5) # return 5, [5, 1] the stack did not change.

            self.assertEqual(stk.pop(), 1) # return 1, [5] the top of the stack and the max element is now 5.
            self.assertEqual(stk.top(), 5) # return 5, [5] the stack did not change.

if __name__ == "__main__":
    unittest.main()
