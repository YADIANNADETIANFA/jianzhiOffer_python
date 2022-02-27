class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:

        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        pMerge = None

        if pHead1.val > pHead2.val:
            pMerge = pHead2
            pMerge.next = self.Merge(pHead1, pHead2.next)
        else:
            pMerge = pHead1
            pMerge.next = self.Merge(pHead1.next, pHead2)

        return pMerge


# 合并两个排序的链表
# 两个指针分别指向两个链表，Merge递归