"""
146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity
- int get(int key) Return the value of the key if the key exists, otherwise return -1
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity

Example1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
"""

"""
Note:
1. Doubly linked list + Hash Table:
(1) addNode
(2) removeNode
(3) get
(4) put
"""

import unittest
class ListNode:
    def __init__(self, key, val,next=None, prev=None) -> None:
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.removeNode(self.lookup[key])
        elif self.capacity == len(self.lookup):
            lru = self.head.next
            self.removeNode(lru)
            del self.lookup[lru.key]
        
        newNode = ListNode(key, value)
        self.addNode(newNode)
        self.lookup[newNode.key] = newNode
        

# Unit Tests

class TestLRUCache(unittest.TestCase):
    def testLRUCache1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), 1)
        lRUCache.put(3, 3)
        self.assertEqual(lRUCache.get(2), -1)
        lRUCache.put(4, 4)
        self.assertEqual(lRUCache.get(1), -1)
        self.assertEqual(lRUCache.get(3), 3)
        self.assertEqual(lRUCache.get(4), 4)
        


if __name__ == "__main__":
    unittest.main()
