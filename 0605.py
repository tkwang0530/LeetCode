"""
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

"""
Note:
1. Greedy: O(n) time | O(1) space - where n is the length of array flowerbed
"""




import unittest
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        total = len(flowerbed)
        for i in range(total):
            prev, current, next = flowerbed[i-1] if i - \
                1 >= 0 else 0, flowerbed[i], flowerbed[i+1] if i+1 < total else 0
            if current == 0 and prev == 0 and next == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0


# Unit Tests
funcs = [Solution().canPlaceFlowers]


class TestCanPlaceFlowers(unittest.TestCase):
    def testCanPlaceFlowers1(self):
        for func in funcs:
            flowerbed = [1, 0, 0, 0, 1]
            n = 1
            self.assertEqual(func(flowerbed=flowerbed, n=n), True)

    def testCanPlaceFlowers2(self):
        for func in funcs:
            flowerbed = [1, 0, 0, 0, 1]
            n = 2
            self.assertEqual(func(flowerbed=flowerbed, n=n), False)


if __name__ == "__main__":
    unittest.main()
