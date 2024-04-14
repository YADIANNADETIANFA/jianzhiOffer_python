class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 空链表
        if head is None or val is None:
            return None
        # 删除的是头节点
        if head.val == val:
            head = head.next
            return head
        # 其余情况，双指针
        first, second = head, head.next
        while first:
            # 遍历一遍链表，发现没有该值
            if second is None:
                return head
            else:
                # 发现了要删除的节点
                if second.val == val:
                    first.next = second.next
                    return head
                else:
                    # 继续后移
                    first = second
                    second = second.next
        return head


# 删除链表的节点
# 这里假设链表的各个节点值都不相等
# 注意这里给的是要删除的节点的值，不是要删除的节点；正常一般都是给要删除的节点本身
# 思路都是一样的，除特殊情况特殊处理外，其余情况都是“双指针”或“将要删除点的下一点的内容，复制给要删除点，删除下一点”
