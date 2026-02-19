# Tests for matchPlayersAndTrainers (LeetCode 2410)
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

from src.matchPlayersAndTrainers import Solution

s = Solution()


def test_example1():
    assert s.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]) == 2


def test_example2():
    assert s.matchPlayersAndTrainers([1, 1, 1], [10]) == 1
