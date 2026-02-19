"""
Two Pointers + BST In-Order Traversal | LeetCode #653

Strategy:
- A BST's in-order traversal yields a sorted array.
- Collect all values via in-order DFS into a list, then apply the classic
  two-pointer two-sum technique on the sorted result.
- Move the left pointer right when the current sum is too small, and the
  right pointer left when it is too large.

Time Complexity: O(n) — visiting every node once for traversal, then O(n)
for the two-pointer scan; n = number of nodes.
Space Complexity: O(n) — storing all node values in the list, plus O(h)
implicit call stack for recursion where h is the tree height.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        vals = list()
        dummy = root
        self.in_order(dummy, vals)

        l = 0
        r = len(vals) - 1

        while l < r:
            the_sum = vals[l] + vals[r]
            if the_sum == k:
                return True
            if k > the_sum:
                l += 1
            else:
                r -= 1
        return False

    def in_order(self, dummy: TreeNode | None, l: list):
        if dummy is None:
            return

        self.in_order(dummy.left, l)
        l.append(dummy.val)
        self.in_order(dummy.right, l)
