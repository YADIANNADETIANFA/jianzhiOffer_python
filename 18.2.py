class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:

        # 虚拟头结点dummy
        dummy = ListNode(-1)

        # tail表示当前有效链表的尾节点
        tail = dummy

        while pHead is not None:

            # 在正常情况下，首次遇到不同节点，可将其纳入
            # （1）
            if pHead.next is None or pHead.val != pHead.next.val:
                tail.next = pHead
                tail = pHead

            # 越过重复节点
            while pHead.next is not None and pHead.val == pHead.next.val:
                pHead = pHead.next

            # （2）
            pHead = pHead.next

        # 必须保留，否则{1,1,2,3,3,4,5,5}结果为{2,4,5,5}，而非{2,4}
        tail.next = None
        return dummy.next


if __name__ == '__main__':
    solution = Solution()

    listNode_1 = ListNode(1)
    listNode_2 = ListNode(1)
    listNode_3 = ListNode(2)
    listNode_4 = ListNode(3)
    listNode_5 = ListNode(3)
    listNode_6 = ListNode(4)
    listNode_7 = ListNode(5)
    listNode_8 = ListNode(5)

    listNode_1.next = listNode_2
    listNode_2.next = listNode_3
    listNode_3.next = listNode_4
    listNode_4.next = listNode_5
    listNode_5.next = listNode_6
    listNode_6.next = listNode_7
    listNode_7.next = listNode_8

    res = solution.deleteDuplication(listNode_1)

# 以[1,2,3,3,4,4,5]为例，（1）和（2）共同保证了最终结果为[1,2,5]，而非[1,2,4,5]这种情况

# 删除链表中重复的节点