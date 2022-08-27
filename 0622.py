"""
622. Design Circular Queue
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the CircularQueue class:
- CircularQueue() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Example1:
Input
["CircularQueue", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
CircularQueue stk = new CircularQueue();
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
1. Two Pointers
All Methods Time: O(1)
All Methods Space: O(1)
"""

# The circular queue is a linear data structure follow FIFO principle
class MyCircularQueue:

    # Initialize the object with the size of the queue to be k.
    def __init__(self, k: int):
        self.nums = [-1] * k
        self.frontIdx = self.rearIdx = 0
        self.count = 0

    # Inserts an element into the circular queue. Return true if the operation is successful
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.nums[self.rearIdx] = value
        self.rearIdx = (self.rearIdx + 1) % len(self.nums)
        self.count += 1
        return True

    # Deletes an element from the circular queue. Return true if the operation is successful
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.nums[self.frontIdx] = -1
        self.frontIdx = (self.frontIdx + 1) % len(self.nums)
        self.count -= 1
        return True

    # Gets the front item from the queue. If the queue is empty, return -1
    def Front(self) -> int:
        return self.nums[(self.frontIdx) % len(self.nums)]
        
    # Gets the last item from the queue. If the queue is empty, return -1
    def Rear(self) -> int:
        return self.nums[(self.rearIdx-1+len(self.nums)) % len(self.nums)]
        
    # Checks whether the circular queue is empty or not
    def isEmpty(self) -> bool:
        return self.count == 0

    # Checks whether the circular queue is full or not
    def isFull(self) -> bool:
        return self.count == len(self.nums)

# Unit Tests
import unittest

class TestCircularQueue(unittest.TestCase):
    def testCircularQueue1(self):
        myCircularQueue = MyCircularQueue(3)
        self.assertEqual(myCircularQueue.enQueue(1), True)
        self.assertEqual(myCircularQueue.enQueue(2), True)
        self.assertEqual(myCircularQueue.enQueue(3), True)
        self.assertEqual(myCircularQueue.enQueue(4), False)
        self.assertEqual(myCircularQueue.Rear(), 3)
        self.assertEqual(myCircularQueue.isFull(), True)
        self.assertEqual(myCircularQueue.deQueue(), True)
        self.assertEqual(myCircularQueue.enQueue(4), True)
        self.assertEqual(myCircularQueue.Rear(), 4)

if __name__ == "__main__":
    unittest.main()
