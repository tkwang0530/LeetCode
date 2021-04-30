import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i, num in enumerate(nums):
            if target - num in dict:
                return [i, dict[target - num]]
            else:
                dict[num] = i
        return


# Testing
class TestTwoSum(unittest.TestCase):
    def testTwoSum1(self):
        sol = Solution()

        self.assertEqual(
            sol.twoSum(nums=[2, 7, 11, 15], target=9).sort(), [1, 0].sort()
        )

    def testTwoSum2(self):
        sol = Solution()
        self.assertEqual(sol.twoSum(nums=[3, 2, 4], target=6).sort(), [1, 2].sort())


if __name__ == "__main__":
    unittest.main()