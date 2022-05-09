"""
341. Flatten Nested List Iterator
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:
- NestedIterator(List<NestedInteger> nestedList) Initialize the iterator with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Your code will be tested with the following pseudocode:
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

if res matches the expected flatten list, then your code will be judged as correct.

Example1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10^6, 10^6].
"""

"""
Note:
1. Using Stack + Reverse List:
Total Space Complexity: O(n)
Time Complexity:
__init__: O(1)
next: O(1) in average
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List
class NestedInteger:
    def __init__(self, input):
        self.input = input
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return str(self.input)[0].isdigit()

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.input if self.isInteger() else None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.input if not self.isInteger() else None

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False

# Unit Tests
import unittest
classes = [NestedIterator]

class TestNestedIterator(unittest.TestCase):
    def testNestedIterator1(self):
        for myclass in classes:
            nestedList = [NestedInteger([NestedInteger(1),NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
            nestedIterator = myclass(nestedList)
            res = []
            while nestedIterator.hasNext():
                res.append(nestedIterator.next())
            self.assertEqual(res, [1,1,2,1,1])
    
    def testNestedIterator2(self):
        for myclass in classes:
            nestedList = [NestedInteger(1),NestedInteger([NestedInteger(4),NestedInteger([NestedInteger(6)])])]
            nestedIterator = myclass(nestedList)
            res = []
            while nestedIterator.hasNext():
                res.append(nestedIterator.next())
            self.assertEqual(res, [1,4,6])
        


if __name__ == "__main__":
    unittest.main()
