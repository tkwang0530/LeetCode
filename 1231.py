"""
1231. Divide Chocolate
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with you k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and given the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example1:
Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example2:
Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example3:
Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]

Constraints:
0 <= k < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
"""

"""
Note:
1. Binary Search: O(nlogn) time | O(1) space
"""

from typing import List
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def condition(sweet) -> bool:
            currentSum = currentK = 0
            for s in sweetness:
                currentSum += s
                if currentSum >= sweet:
                    currentSum = 0
                    currentK += 1
                if currentK >= k+1:
                    return True
            return currentK >= k+1
        
        left, right = min(sweetness), sum(sweetness) + 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

# Unit Tests
import unittest
funcs = [Solution().maximizeSweetness]
class TestMaximizeSweetness(unittest.TestCase):
    def testMaximizeSweetness1(self):
        for func in funcs:
            sweetness = [1,2,3,4,5,6,7,8,9]
            k = 5
            self.assertEqual(func(sweetness=sweetness, k=k), 6)

    def testMaximizeSweetness2(self):
        for func in funcs:
            sweetness = [5,6,7,8,9,1,2,3,4]
            k = 8
            self.assertEqual(func(sweetness=sweetness, k=k), 1)

    def testMaximizeSweetness3(self):
        for func in funcs:
            sweetness = [1,2,2,1,2,2,1,2,2]
            k = 2
            self.assertEqual(func(sweetness=sweetness, k=k), 5)


if __name__ == "__main__":
    unittest.main()
