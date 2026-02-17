# Tests for LeetCode 160 - Intersection of Two Linked Lists
# pytest tests/getIntersectionNode_test.py

from src.getIntersectionNode import ListNode, Solution

s = Solution()


def make_list(vals: list) -> ListNode:
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        node = ListNode(v)
        cur.next = node  # type: ignore[assignment]
        cur = node
    return dummy.next  # type: ignore[return-value]


def test_example1():
    # intersectVal = 8, A = [4,1,8,4,5], B = [5,6,1,8,4,5]
    shared = make_list([8, 4, 5])
    headA = make_list([4, 1])
    headA.next.next = shared  # type: ignore[union-attr, assignment]
    headB = make_list([5, 6, 1])
    headB.next.next.next = shared  # type: ignore[union-attr, assignment]
    assert s.getIntersectionNode(headA, headB) is shared


def test_example2():
    # intersectVal = 2, A = [1,9,1,2,4], B = [3,2,4]
    shared = make_list([2, 4])
    headA = make_list([1, 9, 1])
    headA.next.next.next = shared  # type: ignore[union-attr, assignment]
    headB = make_list([3])
    headB.next = shared  # type: ignore[assignment]
    assert s.getIntersectionNode(headA, headB) is shared


def test_example3():
    # no intersection, A = [2,6,4], B = [1,5]
    headA = make_list([2, 6, 4])
    headB = make_list([1, 5])
    assert s.getIntersectionNode(headA, headB) is None


def test_example4():
    # intersectVal = 2, A = [2,2,4,5,4], B = [2,4,5,4]
    shared = make_list([2, 4, 5, 4])
    headA = make_list([2])
    headA.next = shared  # type: ignore[assignment]
    headB = shared
    assert s.getIntersectionNode(headA, headB) is shared
