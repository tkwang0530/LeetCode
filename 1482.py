"""
1482. Minimum Number of Days to Make m Bouquets
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the i-th flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Example1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

Constraints:
bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n
"""

""" 
1. Binary Search + Sliding Window: O(nlogm) time | O(1) space - where n is the length of bloomDay and m is max(bloomDay)
"""
from typing import List
class Solution(object):
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def hasEnoughBouquets(day) -> bool:
            start = -1
            bouquets = 0
            for end in range(len(bloomDay)):
                isBloom = day >= bloomDay[end]
                if isBloom and start == -1:
                    start = end

                if not isBloom:
                    start = -1
                    continue
                if end - start + 1 == k:
                    bouquets += 1
                    if bouquets == m:
                        return True
                    start = -1
                    continue
            return False

        if len(bloomDay) < m * k:
            return -1
            
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if hasEnoughBouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Unit Tests
import unittest
funcs = [Solution().minDays]


class TestMinDays(unittest.TestCase):
    def testMinDays1(self):
        for func in funcs:
            bloomDay = [1,10,3,10,2]
            m = 3
            k = 1
            self.assertEqual(func(bloomDay=bloomDay, m=m, k=k), 3)

    def testMinDays2(self):
        for func in funcs:
            bloomDay = [1,10,3,10,2]
            m = 3
            k = 2
            self.assertEqual(func(bloomDay=bloomDay, m=m, k=k), -1)
    
    def testMinDays3(self):
        for func in funcs:
            bloomDay = [7,7,7,7,12,7,7]
            m = 2
            k = 3
            self.assertEqual(func(bloomDay=bloomDay, m=m, k=k), 12)

if __name__ == "__main__":
    unittest.main()
