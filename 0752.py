"""
752. Open the Lock
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

Constraints:
1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

"""
Note:
1. BFS: O(10^4) time | O(10^4) space
"""




from typing import List
import unittest
import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendSet = set(deadends)
        if "0000" in deadendSet:
            return -1

        directions = []
        for position in range(4):
            for sign in (1, -1):
                directions.append((position, sign))

        queue = collections.deque([("0000", 0)])
        visited = {"0000"}
        while queue:
            currentStr, step = queue.popleft()
            if currentStr == target:
                return step

            digits = [int(char) for char in list(currentStr)]
            for position, sign in directions:
                temp = digits[position]
                digits[position] = (digits[position]+sign+10) % 10
                nextStr = "".join([str(d) for d in digits])
                digits[position] = temp

                if nextStr in visited or nextStr in deadends:
                    continue
                visited.add(nextStr)
                queue.append((nextStr, step+1))

        return -1


# Unit Tests
funcs = [Solution().openLock]


class TestOpenLock(unittest.TestCase):
    def testOpenLock1(self):
        for func in funcs:
            deadends = ["0201", "0101", "0102", "1212", "2002"]
            target = "0202"
            self.assertEqual(func(deadends=deadends, target=target), 6)

    def testOpenLock2(self):
        for func in funcs:
            deadends = ["8888"]
            target = "0009"
            self.assertEqual(func(deadends=deadends, target=target), 1)

    def testOpenLock3(self):
        for func in funcs:
            deadends = ["8887", "8889", "8878",
                        "8898", "8788", "8988", "7888", "9888"]
            target = "8888"
            self.assertEqual(func(deadends=deadends, target=target), -1)


if __name__ == "__main__":
    unittest.main()
