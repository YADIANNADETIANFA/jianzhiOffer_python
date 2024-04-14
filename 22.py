class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def findKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        if k is None or k < 1 or pHead is None:
            return None

        # 初始化双指针
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

# 相关问题：求链表的中间节点。如果链表中的节点总数为奇数，则返回中间节点，如果节点数总数偶数，则返回中间两个节点的任意一个
# 使用双指针。一个指针一次走一步；一个指针一次走两步
