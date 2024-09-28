"""
641. Design Circular Deque
description: https://leetcode.com/problems/design-circular-deque/description/
"""

"""
Note:
1. Two Pointers:
All operations is O(1) time / O(1) space
except for __init__ O(k) time/ O(k) space
"""
import unittest
class MyCircularDeque:

    def __init__(self, k: int):
        self.h = k-1
        self.t = 0
        self.count = 0
        self.nums = [-1] * k
        self.k = k   

    def insertFront(self, value: int) -> bool:
        if self.count == self.k:
            return False
        
        newH = (self.k + self.h - 1) % self.k
        self.nums[self.h] = value
        self.h = newH
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.k:
            return False

        newT = (self.t + 1) % self.k
        self.nums[self.t] = value
        self.t = newT 
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        
        newH = (self.h + 1) % self.k
        self.nums[newH] = -1
        self.h = newH
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False        
        newT = (self.k + self.t - 1) % self.k
        self.nums[newT] = -1
        self.t = newT
        self.count -= 1
        return True

    def getFront(self) -> int:
        newH = (self.h + 1) % self.k
        return self.nums[newH]

    def getRear(self) -> int:
        newT = (self.k + self.t - 1) % self.k
        return self.nums[newT]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

# Unit Tests
classes = [MyCircularDeque]

class TestMyCircularDeque(unittest.TestCase):
    def testMyCircularDeque1(self):
        for myclass in classes:
           myCircularDeque = MyCircularDeque(3)
           
           self.assertTrue(myCircularDeque.insertLast(1))
           self.assertTrue(myCircularDeque.insertLast(2))
           self.assertTrue(myCircularDeque.insertFront(3))
           self.assertFalse(myCircularDeque.insertFront(4))
           self.assertEqual(2, myCircularDeque.getRear())
           self.assertTrue(myCircularDeque.isFull())
           self.assertTrue(myCircularDeque.deleteLast())
           self.assertTrue(myCircularDeque.insertFront(4))
           self.assertEqual(4, myCircularDeque.getFront())
            
            
            
            
            
            
            
            
            
        


if __name__ == "__main__":
    unittest.main()
