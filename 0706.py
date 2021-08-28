"""
706. Design HashMap
Design a HashMap without using any built-in hash table libraries.

Implement MyHashMap class:
- MyHashMap() initialize the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
- int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:
0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
"""

"""
Note:
1. Open Hashing & LinkedList Node: O(1) time | O(n) space
"""




import unittest
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 2069
        self.bucket = [None] * self.keyRange
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucketIndex = key % self.keyRange
        curr = self.bucket[bucketIndex]
        if not curr:
            self.bucket[bucketIndex] = ListNode(key, value)
            return
        while curr:
            if curr.key == key:
                curr.val = value
                return
            if curr.next:
                curr = curr.next
            else:
                curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucketIndex = key % self.keyRange
        curr = self.bucket[bucketIndex]
        if not curr:
            return -1
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucketIndex = key % self.keyRange
        curr = self.bucket[bucketIndex]
        if not curr:
            return
        if curr.key == key:
            self.bucket[bucketIndex] = curr.next
            return
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

# Unit Tests

class TestMyHashMap(unittest.TestCase):
    def testMyHashMap1(self):
        myHashMap = MyHashMap()
        myHashMap.put(1,1)
        myHashMap.put(2,2)
        self.assertEqual(myHashMap.get(1), 1)
        self.assertEqual(myHashMap.get(3), -1)
        myHashMap.put(2, 1)
        self.assertEqual(myHashMap.get(2), 1)
        myHashMap.remove(2)
        self.assertEqual(myHashMap.get(2), -1)


if __name__ == "__main__":
    unittest.main()
