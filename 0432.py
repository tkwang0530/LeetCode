"""
432. All O`one Data Structure
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:
- AllOne() Initializes the object of the data structure.
- inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
- dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
- getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
- getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

Note that each function must run in O(1) average time complexity.

Example1:
Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"

Constraints:
1 <= key.length <= 10
key consists of lowercase English letters
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey.
"""

"""
Note:
1. HashTable+BST
Time:
    __init__: O(1)
    inc: amortized O(1) 
    dec: amortized O(1)
    getMaxKey: O(1)
    getMinKey: O(1)
Space: O(1)
"""

import collections
from sortedcontainers import SortedList
class AllOne:

    # __init__ initializes the object of the data structure
    def __init__(self):
        self.keyCounts = collections.defaultdict(int)
        self.countKeys = collections.defaultdict(set)
        self.sortedList = SortedList()
        self.minCount = -1
        self.maxCount = -1

    # inc increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
    def inc(self, key: str) -> None:
        self._updateKeyCount(key, 1)
        return

    # dec decrements the count of the string key by 1.
    # If the count of key is 0 after the decrement, remove it from the data structure.
    # It is guaranteed that key exists in the data structure before the decrement.
    def dec(self, key: str) -> None:
        self._updateKeyCount(key, -1)
        return

    # getMaxKey returns one of the keys with the maximal count. If no element exists, return an empty string "".
    def getMaxKey(self) -> str:
        if self._isEmpty():
            return ""
        maxKey = self.countKeys[self.maxCount].pop()
        self.countKeys[self.maxCount].add(maxKey)
        return maxKey
        
    # getMinKey returns one of the keys with the minimum count. If no element exists, return an empty string "".
    def getMinKey(self) -> str:
        if self._isEmpty():
            return ""
        minKey = self.countKeys[self.minCount].pop()
        self.countKeys[self.minCount].add(minKey)
        return minKey
        
    def _updateKeyCount(self, key, count) -> None:
        if key not in self.keyCounts:
            self.countKeys[0].add(key)
            self.minCount = 1
        originalCount = self.keyCounts[key]
        self.keyCounts[key] += count
        currentCount = self.keyCounts[key]
        
        self.countKeys[originalCount].remove(key)
        
        
        self.minCount = self.minCount if self.minCount != -1 else currentCount
        self.maxCount = self.maxCount if self.maxCount != -1 else currentCount
        
        if currentCount > 0:
            self.countKeys[currentCount].add(key)
            if len(self.countKeys[currentCount]) == 1:
                self.sortedList.add(currentCount)
        if originalCount > 0:
            if len(self.countKeys[originalCount]) == 0:
                self.sortedList.remove(originalCount)
               
        self._updateMinMaxCount(originalCount, currentCount)

        
        if len(self.countKeys[originalCount]) == 0:
            del self.countKeys[originalCount]
        if currentCount == 0:
            del self.keyCounts[key]
        
    def _isEmpty(self) -> bool:
        return len(self.keyCounts) == 0
    
    def _updateMinMaxCount(self, originalCount, currentCount):
        isInc = currentCount > originalCount
        if isInc:
            # min could reduce when insert new key
            if currentCount == 1:
                self.minCount = 1
            # 
            elif self.minCount == originalCount and not self.countKeys[originalCount]:
                self.minCount = currentCount
            self.maxCount = max(self.maxCount, currentCount)
        else:
            # min could increase when count reduced to zero
            if self.minCount == originalCount and not self.countKeys[originalCount] and currentCount == 0:
                self.minCount = self.sortedList[0]
            elif self.minCount == originalCount and currentCount > 0:
                self.minCount = currentCount
            
            if self.maxCount == originalCount and not self.countKeys[originalCount]:
                self.maxCount = currentCount

# Unit Tests
import unittest

classes = [AllOne]
class TestAllOne(unittest.TestCase):
    def testAllOne1(self):
        for myclass in classes: 
            allOne = myclass()
            allOne.inc("hello")
            allOne.inc("hello")
            self.assertEqual(allOne.getMaxKey(), "hello") # return "hello"
            self.assertEqual(allOne.getMinKey(), "hello") # return "hello"
            allOne.inc("leet")
            self.assertEqual(allOne.getMaxKey(), "hello")
            self.assertEqual(allOne.getMinKey(), "leet")

if __name__ == "__main__":
    unittest.main()
