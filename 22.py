class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        if k is None or k < 1 or pHead is None:
            return None
        p_left = pHead
        temp = k
        p_right = pHead
        while temp > 0:
            if p_right is not None:
                p_right = p_right.next
                temp -= 1
            else:
                return None

        while p_right is not None:
            p_left = p_left.next
            p_right = p_right.next

        return p_left


# 链表中倒数最后k个节点

# 使用间隔为k的双指针