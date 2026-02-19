# Tests for findTarget.py
# LeetCode: Two Sum IV - Input is a BST

from src.findTarget import Solution, TreeNode

s = Solution()


def make_tree(vals: list, i: int = 0) -> TreeNode | None:
    if i >= len(vals) or vals[i] is None:
        return None
    node = TreeNode(vals[i])
    node.left = make_tree(vals, 2 * i + 1)
    node.right = make_tree(vals, 2 * i + 2)
    return node


def test_example1():
    # [5,3,6,2,4,null,7], k = 9
    root = make_tree([5, 3, 6, 2, 4, None, 7])
    assert s.findTarget(root, 9) is True


def test_example2():
    # [5,3,6,2,4,null,7], k = 28
    root = make_tree([5, 3, 6, 2, 4, None, 7])
    assert s.findTarget(root, 28) is False
