class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        # 虚拟头节点dummy
        dummy = ListNode(-1)

        # tail表示当前有效链表的尾节点
        tail = dummy

        while pHead is not None:
            # 在正常情况下，首次遇到不同节点，可将其纳入
            # (1)
            if pHead.next is None or pHead.val != pHead.next.val:
                tail.next = pHead
                tail = tail.next

            # 越过重复节点
            while pHead.next is not None and pHead.val == pHead.next.val:
                pHead = pHead.next

            # (2)
            pHead = pHead.next

        # 必须保留，否则[1, 1, 2, 3, 3, 4, 5, 5] 结果为 [2, 4, 5, 5]，而不是[2, 4]
        tail.next = None
        return dummy.next


# JZ76，删除链表中重复的结点
