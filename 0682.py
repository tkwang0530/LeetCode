"""
682. Baseball Game
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the i-th operation you must apply to the record and is one of the following:
- An integer x => Record a new score of x.
- '+' => Record a new score that is the sum of the previous two scores
- 'D' => Record a new score that is the double of the previous score.
- 'C' => Invalidate the previous score, removing it from the record.

Example1:
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

Example2:
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

Example3:
Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.

Constraints:
1 <= operations.length <= 1000
operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
For operation "+", there will always be at least two previous scores on the record.
For operations "C" and "D", there will always be at least one previous score on the record.
"""

"""
Note:
1. Brute-Force: O(n) time | O(n) space - where n is the length of array operations
"""




import unittest
from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op == "+":
                if len(records) < 2:
                    records.append(sum(records))
                else:
                    records.append(records[-2]+records[-1])
            elif op == "D":
                records.append(records[-1]*2)
            elif op == "C":
                records.pop()
            else:
                records.append(int(op))
        return sum(records)


# Unit Tests
funcs = [Solution().calPoints]


class TestCalPoints(unittest.TestCase):
    def testCalPoints1(self):
        for func in funcs:
            operations = ["5", "2", "C", "D", "+"]
            self.assertEqual(func(operations=operations), 30)

    def testCalPoints2(self):
        for func in funcs:
            operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
            self.assertEqual(func(operations=operations), 27)

    def testCalPoints3(self):
        for func in funcs:
            operations = ["1", "C"]
            self.assertEqual(func(operations=operations), 0)


if __name__ == "__main__":
    unittest.main()
