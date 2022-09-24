"""
895. Maximum Frequency Stack
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:
- FreqStack() constructs an empty frequency stack.
- void push(int val) pushes an integer val onto the top of the stack.
- int pop() removes and returns the most frequent element in the stack.
    - if there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Example1:
Input
Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

Constraints:
0 <= val <= 10^9
At most 2 * 10^4 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
"""

"""
Note:
1. HashTables: O(1) time | O(1) space
"""




import collections
import unittest
class FreqStack:

    # __init__ constructs an empty frequency stack.
    def __init__(self):
        self.valCount = collections.defaultdict(int)
        self.layerVals = collections.defaultdict(list)
        self.maxCount = 0

    # push pushes an integer val onto the top of the stack.
    def push(self, val: int) -> None:
        self.valCount[val] += 1
        layer = self.valCount[val]
        self.layerVals[layer].append(val)
        self.maxCount = max(self.maxCount, layer)

    # pop removes and returns the most frequent element in the stack.
    # if there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
    def pop(self) -> int:
        val = self.layerVals[self.maxCount].pop()
        self.valCount[val] -= 1
        if len(self.layerVals[self.maxCount]) == 0:
            del self.layerVals[self.maxCount]
            self.maxCount -= 1
        return val


# Unit Tests
class TestATM(unittest.TestCase):
    def testATM1(self):
        freqStack = FreqStack()
        freqStack.push(5)  # The stack is [5]
        freqStack.push(7)  # The stack is [5,7]
        freqStack.push(5)  # The stack is [5,7,5]
        freqStack.push(7)  # The stack is [5,7,5,7]
        freqStack.push(4)  # The stack is [5,7,5,7,4]
        freqStack.push(5)  # The stack is [5,7,5,7,4,5]

        # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
        self.assertEqual(freqStack.pop(), 5)

        # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
        self.assertEqual(freqStack.pop(), 7)

        # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
        self.assertEqual(freqStack.pop(), 5)

        # / return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
        self.assertEqual(freqStack.pop(), 4)


if __name__ == "__main__":
    unittest.main()
