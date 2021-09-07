"""
486. Predict the Winner
You are given an integer array nums. Two players are playing a game with this array: player 1 and palyer 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length-1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

Example1:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.

Example2:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
"""

"""
Note:
1. Recursion: O(2^n) time | O(n) space
2. Recursion with Memorization: O(n^2) time | O(n) space
"""

from typing import Dict, List
import unittest
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.getScore(nums, 0, len(nums) - 1) >= 0
        
    def getScore(self, nums: List[int], left: int, right: int) -> int:
        if left == right: return nums[left]
        return max(
            nums[left] - self.getScore(nums, left+1, right),
            nums[right] - self.getScore(nums, left, right - 1)
        )
    
    def PredictTheWinner2(self, nums: List[int]) -> bool:
        cache = {}
        return self.getScore2(nums, cache, 0, len(nums) - 1) >= 0

    def getScore2(self, nums: List[int], cache: Dict, left: int, right: int) -> int:
        if (left, right) in cache:
            return cache[(left, right)]
        if left == right:
            cache[(left, right)] = nums[left]
        else:
            cache[(left, right)] = max(
                nums[left] - self.getScore2(nums, cache, left + 1, right),
                nums[right] - self.getScore2(nums, cache, left, right - 1)
            )
        return cache[(left, right)]


# Unit Tests
funcs = [Solution().PredictTheWinner, Solution().PredictTheWinner2]


class TestPredictTheWinner(unittest.TestCase):
    def testPredictTheWinner1(self):
        for func in funcs:
            nums = [1,5,2]
            self.assertEqual(func(nums=nums), False)

    def testPredictTheWinner2(self):
        for func in funcs:
            nums = [1, 5, 233, 7]
            self.assertEqual(func(nums=nums), True)

if __name__ == "__main__":
    unittest.main()
