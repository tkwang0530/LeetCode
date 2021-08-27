"""
225. Implement Stack using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
- void push (int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

- You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.

- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

Follow-up: Can you implement the stack using only one queue?
"""

"""
Note:
1. Using two queues (push O(1))
pop(), top()
(0) if length of q2 > 0, return p2.popleft or q2[0] directly
(1) q2.append(q1.pop()) until q1 only has one item
(2) q1, q2 = q2, q1
(3) return q2.popleft or q2[0]

2. Using two queues (push O(n))
push(x)
(1) q1.append(x)
(2) q1.append(q2.popleft()) until q2 has no items
(3) q1, q2 = q2, q1

pop(), top()
return q2.popleft() or q2[0]

3. Using one queue (push O(n))
push(x)
(1) q1.append(x)
(2) q1.append(q1.popleft()) len(q1) - 1 times
"""



from collections import deque
import unittest
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.q2) > 0:
            self.q1.append(self.q2.popleft())
        self.q1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.q2) > 0:
            return self.q2.popleft()
        self.move()
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.popleft()
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.q2) > 0:
            return self.q2[0]
        self.move()
        self.q1, self.q2 = self.q2, self.q1
        return self.q2[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0 and len(self.q2) == 0
        
    def move(self) -> None:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())


class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self.move()
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q2.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q2[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q2) == 0
    
    def move(self) -> None:
        while len(self.q2) > 0:
            self.q1.append(self.q2.popleft())

class MyStack3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        for _ in range(len(self.q1) - 1):
            self.q1.append(self.q1.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0

# Unit Tests
classes = [MyStack, MyStack2, MyStack3]
class TestMyStack(unittest.TestCase):
    def testMyStack1(self):
        for myclass in classes:
            myStack = myclass()
            myStack.push(1)
            myStack.push(2)
            self.assertEqual(myStack.top(), 2)
            self.assertEqual(myStack.pop(), 2)
            self.assertEqual(myStack.empty(), False)
            self.assertEqual(myStack.pop(), 1)
            self.assertEqual(myStack.empty(), True)


if __name__ == "__main__":
    unittest.main()
