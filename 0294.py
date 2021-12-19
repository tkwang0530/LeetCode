"""
294. Flip Game II
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return true if the starting player can guarantee a win, and false otherwise.

Example1:
Input: currentState = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Example2:
Input: currentState = "+"
Output: false

Constraints:
1 <= currentState.length <= 60

Follow up: Derive your algorithm's runtime complexity
"""

"""
Note:
1. dfs + memo
"""

from typing import List
class Solution(object):
    def canWin(self, currentState: str) -> bool:
        memo = {}
        return self.dfs(currentState, True, memo)

    def play(self, currentState) -> List[int]:
        indices = []
        for i in range(len(currentState) - 1):
            if currentState[i] == currentState[i+1] == "+":
                indices.append(i)
        return indices

    # dfs will return true if player one win the game
    def dfs(self, currentState, isPlayerOne, memo) -> bool:
        if currentState in memo:
            return memo[currentState] if isPlayerOne else not memo[currentState]

        indices = self.play(currentState)
        if isPlayerOne:
            isPlayerOneWin = False
            for i in indices:
                isPlayerOneWin = isPlayerOneWin or self.dfs(currentState[:i] + "--" + currentState[i+2:], not isPlayerOne, memo)
                if isPlayerOneWin:
                    break
        else: # isPlayerTwo
            isPlayerTwoWin = True
            for i in indices:
                isPlayerTwoWin = isPlayerTwoWin and self.dfs(currentState[:i] + "--" + currentState[i+2:], not isPlayerOne, memo)

        memo[currentState] = isPlayerOneWin if isPlayerOne else not isPlayerTwoWin
        return memo[currentState] if isPlayerOne else not memo[currentState]





# Unit Tests
import unittest
funcs = [Solution().canWin]


class TestCanWin(unittest.TestCase):
    def testCanWin1(self):
        for func in funcs:
            currentState = "++++"
            self.assertEqual(func(currentState=currentState), True)

    def testCanWin2(self):
        for func in funcs:
            currentState = "+"
            self.assertEqual(func(currentState=currentState), False)

    def testCanWin3(self):
        for func in funcs:
            currentState = "++"
            self.assertEqual(func(currentState=currentState), True)

if __name__ == "__main__":
    unittest.main()
