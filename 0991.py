"""
991. Broken Calculator
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
- multiply the number on display by 2, or
- subtract 1 from the number on display.

Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

Example1:
Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example2:
Input: startValue = 5, target = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example3:
Input: startValue = 3, target = 10
Output: 3
Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
"""

"""
Note:
1. Greedy Algotrithm: O(log(target)) time | O(1) space
Let us go in opposite direction and divide Y by 2 or add 1, to it until we get X.
If X > Y, we do not have a lot of choice, we can just decrease X by one until it becomes equal to Y, so answer will be X - Y.
If X == Y, then we already happy and we can return count
If Y % 2 == 1, then the only choice is subtraction because it can not be multiplication by 2.
If Y % 2 == 0, we always need to divide by 2 in this case
"""




import unittest
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        times = 0
        while target > startValue:
            if target % 2 == 0:
                target = target // 2
            else:
                target += 1
            times += 1
        return times + abs(target - startValue)


# Unit Tests
funcs = [Solution().brokenCalc]


class TestBrokenCalc(unittest.TestCase):
    def testBrokenCalc1(self):
        for func in funcs:
            startValue = 2
            target = 3
            self.assertEqual(func(startValue=startValue, target=target), 2)

    def testBrokenCalc2(self):
        for func in funcs:
            startValue = 5
            target = 8
            self.assertEqual(func(startValue=startValue, target=target), 2)

    def testBrokenCalc3(self):
        for func in funcs:
            startValue = 3
            target = 10
            self.assertEqual(func(startValue=startValue, target=target), 3)


if __name__ == "__main__":
    unittest.main()
