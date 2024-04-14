class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        preNode = None
        pNode = head
        while pNode is not None:
            pNext = pNode.next
            pNode.next = preNode
            preNode = pNode
            pNode = pNext

        return preNode


# 反转链表
# 使用三指针
