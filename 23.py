class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead: ListNode) -> ListNode:

        if pHead is None:
            return None

        pFast = pHead
        pSlow = pHead

        # (1)快慢双指针(一倍速二倍速)，判断是否有环
        # 这里逻辑重点看一下
        while True:
            if pFast is None:
                return None
            pFast = pFast.next
            pSlow = pSlow.next
            if pFast is None:
                return None
            pFast = pFast.next
            if pFast == pSlow:
                break

        # (2)获取环长
        pFast = pFast.next
        length = 1
        while pFast != pSlow:
            pFast = pFast.next
            length += 1

        # (3)获取环入口节点
        # 使用双指针距离length，两指针首次重合点即为环入口
        pSlow = pHead
        pFast = pHead
        while length > 0:
            pFast = pFast.next
            length -= 1

        while pFast != pSlow:
            pSlow = pSlow.next
            pFast = pFast.next

        return pFast


# 链表中环的入口节点
