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
Because we need to remove a data (recently used) from head or from the center and append this data to the tail, I would use doubly linked list to store the key value pairs.

Also we need to return the value accociate with the key efficiently, dictionary will be our choice. And the dictionary will be like lookup<key, node>

for the doublely linked list, I would use two dummy nodes to handle the edge cases

2. OrderedDict
OrderedDict.move_to_end(key)
OrderedDict.popitem(last=False)
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
        self.dummyHead = ListNode(None, None)
        self.dummyTail = ListNode(None, None)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead
    
    def removeNode(self, node):
        next = node.next
        prev = node.prev
        next.prev, prev.next = prev, next
        
    
    def addNode(self, node):
        prev = self.dummyTail.prev
        node.prev = prev
        node.next = self.dummyTail
        prev.next = node
        self.dummyTail.prev = node

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        # remove the node
        node = self.lookup[key]
        self.removeNode(node)
        
        # add node to Tail
        self.addNode(node)
        
        # return the value
        return self.lookup[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            self.removeNode(node)
            
            # modify the node's val before add to the linkedlist
            node.val = value
            self.addNode(node)
        else:
            if len(self.lookup) == self.capacity:
                # in this case, we have to evict the least recently used key
                nodeToRemove = self.dummyHead.next
                self.removeNode(nodeToRemove)
                
                # and we have to delete that key
                del self.lookup[nodeToRemove.key]
            
            # finally we add the key value pair in to our LinkedList and dictionary
            newNode = ListNode(key, value)
            self.addNode(newNode)
            self.lookup[key] = newNode

from collections import OrderedDict
class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, value):
        if key in self.cache: del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    
class LRUCache3:
    # Initialize the LRU cache with positive size capacity.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.dummyHead = ListNode(-1,-1)
        self.dummyTail = ListNode(-1,-1)
        self.dummyHead.next, self.dummyTail.prev = self.dummyTail, self.dummyHead
        self.nodeMap = {} #<key, node>
    
    def __moveToTail(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        beforeTail = self.dummyTail.prev
        beforeTail.next = self.dummyTail.prev = node
        node.prev, node.next = beforeTail, self.dummyTail

    def __evictFromHead(self):
        nodeToRemove = self.dummyHead.next
        afterNode = nodeToRemove.next
        afterNode.prev, self.dummyHead.next = self.dummyHead, afterNode
        self.count -= 1
        del self.nodeMap[nodeToRemove.key]

    def __insertFromTail(self, key: int, val: int):
        newNode = ListNode(key, val)
        beforeTail = self.dummyTail.prev
        beforeTail.next = self.dummyTail.prev = newNode
        newNode.prev, newNode.next = beforeTail, self.dummyTail
        self.nodeMap[key] = newNode
        self.count += 1

    # Return the value of the key if the key exists, otherwise return -1
    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.__moveToTail(node)
        return node.val

        
        
    # Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
    # If the number of keys exceeds the capacity from this operation, evict the least recently used key.  
    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            # update key's val
            nodeToUpdate = self.nodeMap[key]
            nodeToUpdate.val = value
            self.__moveToTail(nodeToUpdate)
            return

        # insert node
        self.__insertFromTail(key, value)

        if self.count > self.capacity:
            self.__evictFromHead()
        


# Unit Tests
classes = [LRUCache, LRUCache2, LRUCache3]

class TestLRUCache(unittest.TestCase):
    def testLRUCache1(self):
        for myclass in classes:
            lRUCache = myclass(2)
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
