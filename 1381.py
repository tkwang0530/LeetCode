"""
1381. Design a Stack With Increment Operation
description: https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
"""

"""
Note:
1. Lazy increment from Lee
Use an additional array to record the increment value.
inc[i] means for all elements stack[0] ~ stack[i],
we should plus inc[i] when popped from the stack.
Then inc[i-1] += inc[i],
so that we can accumulate the increment inc[i] for the bottom elements and the following pop.

__init__: O(1) time | O(1) space
push, pop, increment: O(1) time | O(1) space

2. Lazy increment with fix sized self.inc

3. Lazy increment using HashMap
__init__: O(1) time | O(1) space
push, pop, increment: O(1) time | O(1) space
"""

import collections
class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.inc:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val

class CustomStack2:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        lastIndex = len(self.stack) - 1
        lastInc = self.inc[lastIndex]
        if lastIndex >= 1:
            self.inc[lastIndex-1] += lastInc
        self.inc[lastIndex] = 0
        return self.stack.pop() + lastInc

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.inc[min(k, len(self.stack)) - 1] += val

class CustomStack3:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.increments = collections.defaultdict(int)
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        length = len(self.stack)
        inc = self.increments[length]
        if length > 1:
            self.increments[length-1] += inc
        self.increments[length] = 0
        return inc + self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        length = len(self.stack)
        self.increments[min(length, k)] += val

# Unit Tests
import unittest
classes = [CustomStack, CustomStack2, CustomStack3]

class TestCustomStack(unittest.TestCase):
    def testCustomStack1(self):
        for myclass in classes:
            customStack = myclass(3)
            customStack.push(1) # stack becoms [1]
            customStack.push(2) # stack becomes [1, 2]
            self.assertEqual(customStack.pop(), 2) # return 2 --> Return top of the stack 2, stack becomes [1]
            customStack.push(2) # stack becomes [1, 2]
            customStack.push(3) # stack becomes [1, 2, 3]
            customStack.push(4) # stack still [1, 2, 3], Don't add another elements as size is 4
            customStack.increment(5, 100) # stack become [101, 102, 103]
            customStack.increment(2, 100) # stack become [201, 202, 103]
            self.assertEqual(customStack.pop(), 103)
            self.assertEqual(customStack.pop(), 202)
            self.assertEqual(customStack.pop(), 201)
            self.assertEqual(customStack.pop(), -1)
        


if __name__ == "__main__":
    unittest.main()
