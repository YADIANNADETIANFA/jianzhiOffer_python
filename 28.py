class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    # def isSymmetrical(self, pRoot: TreeNode) -> bool:
    #     if pRoot is None:
    #         return True
    #     return self.isSymmetricalCore(pRoot, pRoot)
    #
    # def isSymmetricalCore(self, pLeft, pRight):
    #     if pLeft is None and pRight is None:
    #         return True
    #     if pLeft is None or pRight is None:
    #         return False
    #     if pLeft.val != pRight.val:
    #         return False
    #     return self.isSymmetricalCore(pLeft.left, pRight.right) and self.isSymmetricalCore(pLeft.right, pRight.left)


    # 迭代
    def isSymmetrical(self, pRoot: TreeNode) -> bool:

        if pRoot is None:
            return True

        my_list = list()
        my_list.extend([pRoot, pRoot])

        while len(my_list) > 0:
            pNode_1 = my_list.pop(0)
            pNode_2 = my_list.pop(0)
            if pNode_1 is None and pNode_2 is None:
                continue
            if pNode_1 is None or pNode_2 is None:
                return False
            if pNode_1.val != pNode_2.val:
                return False
            else:
                my_list.extend([pNode_1.left, pNode_2.right, pNode_1.right, pNode_2.left])

        return True


# 对称的二叉树
# 还有一种方法，即定义一种与前序遍历相反的算法，遍历顺序：根节点->右子节点->左子节点
# 使用前序遍历和新算法分别遍历一次二叉树，分别记录遍历结果的列表。若两列表相同则True，否则False
# 对于这种方法，需考虑二叉树各节点所有值都相等的情况，这样不对称的二叉树所得的两个列表也完全一样。避免的方式：将None节点也作为一个元素存于列表当中