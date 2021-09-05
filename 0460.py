"""
460. LFU Cache
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, return -1.
- void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

Example1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3

Constraints:
0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.
"""

"""
Note:
1. Two Hash Tables <Integer, DLList> freq: O(1) time | O(1) space
{
    1: head <-> (1,1) <-> (2, 2) <-> tail
    2: head <-> (3,2) <-> tail
}

(1) Each key is mapping to the corresponding node (self._node), where we can retrieve the node in O(1) time
(2) Each frequency freq is mapped to a Doubly Linked List (self._freq), where all nodes in the DLList have the same frequency. Moreover, each node will be always inserted in the head (indicating most recently used).
(3) A minimum frequency self._minfreq is maintained to keep track of the minimum frequency of across all nodes in this cache, such that the DLList with the min frequency can always be retrieved in O(1) time.
"""

import unittest
class ListNode:
    def __init__(self, key: int, val: int) -> None:
        self.val = val
        self.key = key
        self.count = 1
        self.prev = None
        self.next = None

class DLList:
    def __init__(self):
        self.dummyHead = ListNode(None, None)
        self.dummyTail = ListNode(None, None)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead
        self._size = 0

    def __len__(self):
        return self._size
    def addHead(self, node) -> None:
        next = self.dummyHead.next
        node.next, node.prev = next, self.dummyHead
        self.dummyHead.next = next.prev = node
        self._size += 1

    def remove(self, node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
        self._size -= 1

    def removeTail(self) -> int:
        prev = self.dummyTail.prev
        self.remove(prev)
        return prev.key

from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity

        self._node = dict() # <key, ListNode>
        self._freq = defaultdict(DLList)
        self._minfreq = 0

    def _update(self, node):
        freq = node.count
        self._freq[freq].remove(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.count += 1
        freq = node.count
        self._freq[freq].addHead(node)
    
    def get(self, key):
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self._capacity == 0:
            return 
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                keyToRemove = self._freq[self._minfreq].removeTail()
                del self._node[keyToRemove]
                self._size -= 1
        
            node = ListNode(key, value)
            self._node[key] = node
            self._freq[1].addHead(node)
            self._minfreq = 1
            self._size += 1

# Unit Tests
classes = [LFUCache]

class TestLFUCache(unittest.TestCase):
    def testLFUCache1(self):
        for myclass in classes:
            lfu = myclass(2)
            lfu.put(1, 1)
            lfu.put(2, 2)
            self.assertEqual(lfu.get(1), 1)
            lfu.put(3, 3)
            self.assertEqual(lfu.get(2), -1)
            self.assertEqual(lfu.get(3), 3)
            lfu.put(4, 4)
            self.assertEqual(lfu.get(1), -1)
            self.assertEqual(lfu.get(3), 3)
            self.assertEqual(lfu.get(4), 4)
        


if __name__ == "__main__":
    unittest.main()
