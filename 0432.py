"""
432. All O`one Data Structure
description: https://leetcode.com/problems/all-oone-data-structure/description/ 
"""

"""
Note:
1. Doubly Linked List + HashTable: 
All operations are O(1) time and O(1) space
"""

import collections
class Node:
    def __init__(self, count):
        self.count = count
        self.prev = None
        self.next = None

class DLList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(float("inf"))
        self.head.next, self.tail.prev = self.tail, self.head
        self.countMap = {0: self.head, float("inf"): self.tail} # <count, Node>
    
    def remove(self, count):
        if count not in self.countMap:
            return
        nodeToRemove = self.countMap[count]
        prev = nodeToRemove.prev
        next = nodeToRemove.next
        prev.next, next.prev = next, prev
        del self.countMap[count]

    # it is guaranteed that count-1 exists in self.countMap
    def add(self, count):
        if count in self.countMap:
            return

        nodeBefore = nodeBeforeNext = None
        if count - 1 in self.countMap:
            nodeBefore = self.countMap[count-1]
            nodeBeforeNext = nodeBefore.next
        else:
            nodeBeforeNext = self.countMap[count+1]
            nodeBefore = nodeBeforeNext.prev
        nodeToAdd = Node(count)
        self.countMap[count] = nodeToAdd
        nodeToAdd.prev, nodeToAdd.next = nodeBefore, nodeBeforeNext
        nodeBefore.next = nodeBeforeNext.prev = nodeToAdd

    def getMin(self):
        if self.head.next == self.tail:
            return 0
        return self.head.next.count

    def getMax(self):
        if self.tail.prev == self.head:
            return 0
        return self.tail.prev.count


class AllOne:

    def __init__(self):
        self.counterKeys = collections.defaultdict(set)
        self.keyCounter = collections.defaultdict(int)
        self.dLList = DLList()

    def inc(self, key: str) -> None:
        oriCount = self.keyCounter[key]
        self.keyCounter[key] += 1
        if oriCount != 0:
            self.counterKeys[oriCount].remove(key)
            
        self.counterKeys[oriCount+1].add(key)

        # maintain dLList
        self.dLList.add(oriCount+1)
        if len(self.counterKeys[oriCount]) == 0 and oriCount > 0:
            self.dLList.remove(oriCount)
        
        

    def dec(self, key: str) -> None:
        oriCount = self.keyCounter[key]
        self.keyCounter[key] -= 1
        if self.keyCounter[key] == 0:
            del self.keyCounter[key]

        self.counterKeys[oriCount].remove(key)
        if oriCount - 1 > 0:
            self.counterKeys[oriCount-1].add(key)
        
        # maintain dLList
        self.dLList.add(oriCount-1)
        if len(self.counterKeys[oriCount]) == 0 and oriCount > 0:
            self.dLList.remove(oriCount)

    def getMaxKey(self) -> str:
        maxCount = self.dLList.getMax()
        if maxCount == 0:
            return ""
        e = self.counterKeys[maxCount].pop()
        self.counterKeys[maxCount].add(e)
        return e

    def getMinKey(self) -> str:
        minCount = self.dLList.getMin()
        if minCount == 0:
            return ""
        e = self.counterKeys[minCount].pop()
        self.counterKeys[minCount].add(e)
        return e
classes = [AllOne]

import unittest
class TestAllOne(unittest.TestCase):
    def testAllOne1(self):
        for myclass in classes:
            allOne = AllOne()
            allOne.inc("hello")
            allOne.inc("hello")
            self.assertEqual(allOne.getMaxKey(), "hello")
            self.assertEqual(allOne.getMinKey(), "hello")
            allOne.inc("leet")
            self.assertEqual(allOne.getMaxKey(), "hello")
            self.assertEqual(allOne.getMinKey(), "leet")

if __name__ == "__main__":
    unittest.main()
