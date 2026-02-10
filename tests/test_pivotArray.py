import unittest
from src.pivotArray import Solution


class TestPivotArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_pivot(self):
        nums = [9, 12, 5, 10, 14, 3, 10]
        pivot = 10
        result = self.solution.pivotArray(nums, pivot)
        self.assertEqual(result, [9, 5, 3, 10, 10, 12, 14])

    def test_2(self):
        nums = [-3, 4, 3, 2]
        pivot = 2
        result = self.solution.pivotArray(nums, pivot)
        self.assertEqual(result, [-3, 2, 4, 3])


if __name__ == "__main__":
    unittest.main()
