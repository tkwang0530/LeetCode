"""
705. Design HashSet
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:
- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:
0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
"""

"""
Note:
1. Open Hashing & LinkedList Node: O(1) time | O(n) space
"""




import unittest
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucket = [None] * self.keyRange
        

    def add(self, key: int) -> None:
        bucketIndex = key % self.keyRange
        curr = self.bucket[bucketIndex]
        if not curr:
            self.bucket[bucketIndex] = ListNode(key)
            return
        while curr:
            if curr.val == key:
                return
            if curr.next:
                curr = curr.next
            else:
                curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        bucketIndex = key % self.keyRange
        curr = self.bucket[bucketIndex]
        if not curr:
            return
        if curr.val == key:
            self.bucket[bucketIndex] = curr.next
            return
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = key % self.keyRange
        curr = self.bucket[bucketIndex]
        if not curr:
            return False
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Unit Tests

class TestMyHashSet(unittest.TestCase):
    def testMyHashSet1(self):
        myHashSet = MyHashSet()
        myHashSet.add(1)
        myHashSet.add(2)
        self.assertEqual(myHashSet.contains(1), True)
        self.assertEqual(myHashSet.contains(3), False)
        myHashSet.add(2)
        self.assertEqual(myHashSet.contains(2), True)
        myHashSet.remove(2)
        self.assertEqual(myHashSet.contains(2), False)


if __name__ == "__main__":
    unittest.main()
