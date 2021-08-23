"""
282. Expression Add Operators
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression to the target value.

Example1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Example2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

Example3:
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example4:
Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]

Example5:
Input: num = "3456237490", target = 9191
Output: []

Constraints:
1 <= num.length <= 10
num consists of only digits
-2^31 <= target <= 2^31 - 1
"""

"""
Note:
1. DFS: O(n* 4^(n-1)) time | O(n) space

"""

from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        if not num or len(num) == 0:
            return result
        self.dfs(result, num, "", target, 0, 0, 0)
        return result

    def dfs(self, result: List[str], num: str, path: str, target: int, index: int, curr: int, prev: int) -> None:
        # Exit
        if index == len(num):
            if curr == target:
                result.append(path)
            return
        
        # divide: digit * operators
        for i in range(index, len(num)):
            if i != index and num[index] == "0": # number more than one digits can't start with "0"
                break

            currStr = num[index: i+1]
            currNum = int(currStr)

            # two cases: first one, not first one
            if index == 0:
                self.dfs(result, num, path + currStr, target, i + 1, currNum, currNum)
            else:
                self.dfs(result, num, path + "+" + currStr, target, i + 1, curr + currNum, currNum)
                self.dfs(result, num, path + '-' + currStr, target, i + 1, curr - currNum, -currNum)
                self.dfs(result, num, path + "*" + currStr, target, i + 1, curr - prev + prev * currNum, prev * currNum)
            

# Unit Tests
import unittest
funcs = [Solution().addOperators]


class TestAddOperators(unittest.TestCase):
    def testAddOperators1(self):
        for func in funcs:
            num = "123"
            target = 6
            self.assertEqual(sorted(func(num=num, target=target)), sorted(["1*2*3","1+2+3"]))

    def testAddOperators2(self):
        for func in funcs:
            num = "232"
            target = 8
            self.assertEqual(sorted(func(num=num, target=target)), sorted(["2*3+2","2+3*2"]))

    def testAddOperators3(self):
        for func in funcs:
            num = "105"
            target = 5
            self.assertEqual(sorted(func(num=num, target=target)), sorted(["1*0+5","10-5"]))

    def testAddOperators4(self):
        for func in funcs:
            num = "00"
            target = 0
            self.assertEqual(sorted(func(num=num, target=target)), sorted(["0*0","0+0","0-0"]))

    def testAddOperators5(self):
        for func in funcs:
            num = "3456237490"
            target = 9191
            self.assertEqual(sorted(func(num=num, target=target)), sorted([]))

if __name__ == "__main__":
    unittest.main()