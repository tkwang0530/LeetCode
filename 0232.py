"""
232. Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push (int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

Example1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
"""

"""
Note:
1. pushStack and popStack: O(1) time | O(n) space
The time complexity is amortized
"""




import unittest
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushStack = []
        self.popStack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pushStack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.popStack) == 0:
            self.move()
        return self.popStack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.popStack) == 0:
            self.move()
        return self.popStack[len(self.popStack) - 1]
            
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.pushStack) == 0 and len(self.popStack) == 0
    
    def move(self) -> None:
        while len(self.pushStack) > 0:
            self.popStack.append(self.pushStack.pop())


# Unit Tests

class TestMyQueue(unittest.TestCase):
    def testMyQueue1(self):
        myQueue = MyQueue()
        myQueue.push(1)
        myQueue.push(2)
        self.assertEqual(myQueue.peek(), 1)
        self.assertEqual(myQueue.pop(), 1)
        self.assertEqual(myQueue.empty(), False)
        self.assertEqual(myQueue.peek(), 2)
        self.assertEqual(myQueue.pop(), 2)
        self.assertEqual(myQueue.empty(), True)


if __name__ == "__main__":
    unittest.main()
