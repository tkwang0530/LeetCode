"""
1286. Iterator for Combination
description: https://leetcode.com/problems/iterator-for-combination/
"""

"""
Note:
1. backtrack: O(2^n * k) time | O(C(n, k) * k) space - where k is combinationLength
"""

import collections
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        n = len(characters)
        k = combinationLength
        current = []
        self.queue = collections.deque([])
        def backtrack(i):
            if len(current) == k:
                self.queue.append("".join(current))
                return

            for j in range(i, n):
                current.append(characters[j])
                backtrack(j+1)
                current.pop()
        backtrack(0)


    def next(self) -> str:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0
        
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Unit Tests
import unittest
classes = [CombinationIterator]


class TestCombinationSum(unittest.TestCase):
    def testCombinationSum1(self):
        for myclass in classes:
            characters = "abc"
            combinationLength = 2
            itr = myclass(characters=characters, combinationLength=combinationLength)
            self.assertEqual(itr.next(), "ab")
            self.assertEqual(itr.hasNext(), True)
            self.assertEqual(itr.next(), "ac")
            self.assertEqual(itr.hasNext(), True)
            self.assertEqual(itr.next(), "bc")
            self.assertEqual(itr.hasNext(), False)

if __name__ == "__main__":
    unittest.main()
