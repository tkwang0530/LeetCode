"""
904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
- You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

Example4:
Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can pick from trees [1,2,1,1,2].

Constraints:
1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space
"""

from typing import List
import unittest

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        currFruits = maxFruits = 0
        basket = {}
        for end in range(len(fruits)):
            currFruits += 1
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1
            while len(basket) > 2:
                currFruits -= 1
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            maxFruits = max(maxFruits, currFruits)
        return maxFruits

# Unit Tests
funcs = [Solution().totalFruit]

class TestTotalFruit(unittest.TestCase):
    def testTotalFruit1(self):
        for func in funcs:
            fruits = [1,2,1]
            self.assertEqual(
                func(fruits=fruits), 3)
    
    def testTotalFruit2(self):
        for func in funcs:
            fruits = [0,1,2,2]
            self.assertEqual(
                func(fruits=fruits), 3)

    def testTotalFruit3(self):
        for func in funcs:
            fruits = [1,2,3,2,2]
            self.assertEqual(
                func(fruits=fruits), 4)

if __name__ == "__main__":
    unittest.main()
