"""
Two Pointers

The naive approach checks every node in A against every node in B to find a
shared reference — O(n*m). We can do better by recognizing that if an
intersection exists, both lists share the same suffix from that point on. The
only reason a simultaneous walk from both heads misses it is that the lists may
have different lengths, so the two pointers arrive at the intersection at
different steps — they're out of phase by |lenA - lenB|.

The redirect trick phases them: when A is exhausted after lenA steps, send it
to B's head; when B is exhausted after lenB steps, send it to A's head. Now A
will reach the intersection after lenA + (lenB - shared) steps, and B will
reach it after lenB + (lenA - shared) steps — the same count. They land on the
intersection simultaneously without ever comparing every pair of nodes.

Time complexity: O(n) where n = lenA + lenB
Space complexity: O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> ListNode | None:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
