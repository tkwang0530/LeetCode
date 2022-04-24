"""
2029. Stone Game IX
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the i-th stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.

Example1:
Input: stones = [2,1]
Output: true
Explanation: The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

Example2:
Input: stones = [2]
Output: false
Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.

Example3:
Input: stones = [5,1,2,4,3]
Output: false
Explanation: Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

Constraints:
1 <= stones.length <= 10^5
1 <= stones[i] <= 10^4
"""

""" 
1. max recursion: O(1) time | O(1) space
"""

from typing import List
class Solution(object):
    def stoneGameIX(self, stones: List[int]) -> bool:
        leftNumbers = [0] * 3
        for stone in stones:
            leftNumbers[stone % 3] += 1
        
        leftNumbers[0] %= 2
        
        
        if leftNumbers[1] > 3 and leftNumbers[2] > 3:
            minNum = min(leftNumbers[1]-3, leftNumbers[2]-3)
            leftNumbers[1] -= minNum
            leftNumbers[2] -= minNum
        
        def dfs(removeSum):
            leftNumberSum = sum(leftNumbers)
            isAliceTurn = leftNumberSum % 2 == len(stones) % 2
            if removeSum == 0:
                return isAliceTurn
            elif leftNumberSum == 0:
                return False
            
            if isAliceTurn:
                canWin = False
                for choice in range(3):
                    if leftNumbers[choice] == 0:
                        continue
                    leftNumbers[choice] -= 1
                    canWin = canWin or dfs((removeSum+choice) % 3)
                    leftNumbers[choice] += 1
            else:
                canWin = True
                for choice in range(3):
                    if leftNumbers[choice] == 0:
                        continue
                    leftNumbers[choice] -= 1
                    canWin = canWin and dfs((removeSum+choice) % 3)
                    leftNumbers[choice] += 1
            
            return canWin
        return dfs(3)


# Unit Tests
import unittest
funcs = [Solution().stoneGameIX]

class TestStoneGameIX(unittest.TestCase):
    def testStoneGameIX1(self):
        for func in funcs:
            stones = [2,1]
            self.assertEqual(func(stones=stones), True)

    def testStoneGameIX2(self):
        for func in funcs:
            stones = [2]
            self.assertEqual(func(stones=stones), False)

    def testStoneGameIX3(self):
        for func in funcs:
            stones = [5,1,2,4,3]
            self.assertEqual(func(stones=stones), False)

    def testStoneGameIX4(self):
        for func in funcs:
            stones = [20,3,20,17,2,12,15,17,4]
            self.assertEqual(func(stones=stones), True)

    def testStoneGameIX5(self):
        for func in funcs:
            stones = [15,20,10,13,14,15,5,2,3]
            self.assertEqual(func(stones=stones), False)

if __name__ == "__main__":
    unittest.main()
