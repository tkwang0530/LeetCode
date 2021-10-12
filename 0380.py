"""
380. Insert Delete GetRandom O(1)
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Example1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

"""
Note:
1. list + Hash Table:
(1) use Hash Table to store the index of each value in the list, and the list to store the value
(2) insert: O(1) time | O(1) space
(3) remove: O(1) time | O(1) space
if val in Hash Table: swap the val with the last val then pop the val out. Besides remove the related key from the Hash Table
(4) getRandom: O(logn) time | O(1) space
we can directly use the random.choice(list), O(logn) time in python
"""

import random
class RandomizedSet:

    def __init__(self):
        self.valueIndice = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        if val in self.valueIndice:
            return False
        self.valueIndice[val] = len(self.numList)
        self.numList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueIndice:
            return False
        valueIndex = self.valueIndice[val]
        originalLastVal = self.numList[-1]
        self.numList[valueIndex], self.numList[-1] = self.numList[-1], self.numList[valueIndex]
        self.valueIndice[originalLastVal] = valueIndex
        self.numList.pop()
        del self.valueIndice[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.numList)

# Unit Tests
import unittest
classes = [RandomizedSet]

class TestRandomizedSet(unittest.TestCase):
    def testRandomizedSet1(self):
        for myclass in classes:
            randomizedSet = myclass()
            self.assertEqual(randomizedSet.insert(1), True)
            self.assertEqual(randomizedSet.remove(2), False)
            self.assertEqual(randomizedSet.insert(2), True)

            self.assertTrue(randomizedSet.getRandom() in (1, 2))
            self.assertEqual(randomizedSet.remove(1), True)
            self.assertEqual(randomizedSet.insert(2), False)

            self.assertEqual(randomizedSet.getRandom(), 2)


if __name__ == "__main__":
    unittest.main()
