"""
838. Push Dominoes
There are n dominoes in a line, and we place each domino vertically upright. In the begining, we simultaneously push some of the dominoes either to the left or to the right. After each second, each domino that is falling to the left pushes the adjacent domino on the left, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:
- dominoes[i] = 'L', if the i-th domino has been pushed to the left,
- dominoes[i] = 'R', if the i-th domino has been pushed to the right, and
- dominoes[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state.

Example1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Constraints:
n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.' .
"""

"""
Note:
1. Sliding Window: O(n) time | O(n) space
2. PreSum from both sides: O(n) time | O(n) space
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        chars = list("L"+dominoes+"R")
        left = 0
        for right in range(len(chars)):
            if chars[right] not in ["L", "R"]:
                continue
            
            leftChar, rightChar = chars[left], chars[right]
            if (leftChar, rightChar) == ("L", "R"):
                left = right
                continue
            
            # "L...L" => O(n) => all . => L
            if (leftChar, rightChar) == ("L", "L"):
                for i in range(left+1, right):
                    chars[i] = "L"
                    left = right
                    continue
            
            # "R...R" => O(n) => all . => R
            if (leftChar, rightChar) == ("R", "R"):
                for i in range(left+1, right):
                    chars[i] = "R"
                    left = right
                    continue
            
            # "R...L" => O(n) => half R half L , mid .
            l, r = left+1, right-1
            while l < r:
                chars[l] = "R"
                chars[r] = "L"
                l += 1
                r -= 1
            left = right
        return "".join(chars[1:len(chars)-1])

    def pushDominoes2(self, dominoes: str) -> str:
        dominoes = list("L" + dominoes + "R")
        n = len(dominoes)

        left = [0] * n # weight, posive weight means falling to right, negative sign means falling to left
        right = [0] * n

        left[0] = -n   # falling to Left: negative sign
        right[-1] = n # falling to Right: positive sign

        for i in range(1, n):
            if dominoes[i] !=  ".":
                left[i] = n if dominoes[i] == "R" else -n
            elif left[i-1] > 0:
                left[i] = left[i-1]-1

        for i in range(n-2, -1, -1):
            if dominoes[i] !=  ".":
                right[i] = n if dominoes[i] == "R" else -n
            elif right[i+1] < 0:
                right[i] = right[i+1]+1

        for i in range(n):
            currentSum = left[i] + right[i]
            if currentSum > 0:
                dominoes[i] = "R"
            elif currentSum < 0:
                dominoes[i] = "L"
            else:
                dominoes[i] = "."
        return "".join(dominoes[1:-1])


# Unit Tests
import unittest
funcs = [Solution().pushDominoes, Solution().pushDominoes2]

class TestPushDominoes(unittest.TestCase):
    def testPushDominoes1(self):
        for func in funcs:
            dominoes = "RR.L"
            self.assertEqual(func(dominoes=dominoes), "RR.L")

    def testPushDominoes2(self):
        for func in funcs:
            dominoes = ".L.R...LR..L.."
            self.assertEqual(func(dominoes=dominoes), "LL.RR.LLRRLL..")


if __name__ == "__main__":
    unittest.main()
