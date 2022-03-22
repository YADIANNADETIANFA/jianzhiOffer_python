import copy

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    # 哈希表法，两次遍历，详细解释见书
    def Clone(self, pHead):
        if pHead is None:
            return None
        my_dict = dict()
        p_copy_head = RandomListNode(pHead.label)
        my_dict[pHead] = p_copy_head
        pNode = pHead
        p_copy_node = p_copy_head

        while pNode is not None:
            pNode = pNode.next
            if pNode is not None:
                p_copy_node.next = RandomListNode(pNode.label)
                p_copy_node = p_copy_node.next
                my_dict[pNode] = p_copy_node

        for key in my_dict.keys():
            my_dict[key].random = my_dict.get(key.random)

        return p_copy_head

    # 使用库函数
    def Clone_2(self, pHead):
        ret = copy.deepcopy(pHead)
        return ret

    # 标准解法：
    # 1、每个节点后添加一个复制节点；
    # 2、再次遍历，设置新加节点的复式指针
    # 3、链表分离，还原原链表，获得新深拷贝链表
    def Clone_3(self, pHead):
        if pHead is None:
            return None

        # 1、每个节点后添加一个复制节点；
        pNode = pHead
        while pNode is not None:
            pTemp = pNode.next
            pNew = RandomListNode(pNode.label)
            pNew.next = pTemp
            pNode.next = pNew
            pNode = pTemp

        # 2、再次遍历，设置新加节点的复式指针
        pNode = pHead
        while pNode is not None:
            pTemp = pNode.next
            pTemp.random = pNode.random
            pNode = pTemp.next

        # 3、链表分离，还原原链表，获得新深拷贝链表
        p_copy_head = pHead.next

        pNode = pHead
        p_copy_node = p_copy_head

        pTemp = p_copy_node.next

        if pTemp is None:
            pHead.next = None
            return p_copy_head

        while pTemp is not None:
            pNode.next = pTemp
            p_copy_node.next = pTemp.next
            pNode = pNode.next
            p_copy_node = p_copy_node.next
            pTemp = pTemp.next.next

        # 还原原链表时，消除倒数第二个节点与倒数第一个节点这两个重复节点间的指针
        pNode.next = None

        res_ori = pHead
        res_new = p_copy_head
        return p_copy_head




if __name__ == '__main__':
    pNode_1 = RandomListNode(1)
    pNode_2 = RandomListNode(2)
    pNode_3 = RandomListNode(3)
    pNode_4 = RandomListNode(4)
    pNode_5 = RandomListNode(5)
    pNode_1.next = pNode_2
    pNode_2.next = pNode_3
    pNode_3.next = pNode_4
    pNode_4.next = pNode_5
    pNode_1.random = pNode_3
    pNode_2.random = pNode_5
    pNode_4.random = pNode_2
    solution = Solution()
    res = solution.Clone_3(pNode_1)


# 复杂链表的复制

# None可以作为dict的键或值
# 注意，对于不存在的键，my_dict[32]将抛KeyError异常；my_dict.get(32)返回None，不抛异常