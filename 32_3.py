from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot: TreeNode) -> List[List[int]]:
        res_list = list()
        if pRoot is None:
            return res_list
        # temp_list_1，temp_list_2当栈使用
        temp_list_1 = list()
        temp_list_2 = list()
        # sign = True:  先压左子，再压右子
        # sign = False: 先压右子，再压左子
        sign = True
        temp_list_1.append(pRoot)
        while len(temp_list_1) > 0 or len(temp_list_2) > 0:
            res_temp_list = list()
            if len(temp_list_1) > 0:
                if sign:
                    while len(temp_list_1) > 0:
                        temp_node = temp_list_1.pop()
                        res_temp_list.append(temp_node.val)
                        if temp_node.left is not None:
                            temp_list_2.append(temp_node.left)
                        if temp_node.right is not None:
                            temp_list_2.append(temp_node.right)
                else:
                    while len(temp_list_1) > 0:
                        temp_node = temp_list_1.pop()
                        res_temp_list.append(temp_node.val)
                        if temp_node.right is not None:
                            temp_list_2.append(temp_node.right)
                        if temp_node.left is not None:
                            temp_list_2.append(temp_node.left)
            else:
                if sign:
                    while len(temp_list_2) > 0:
                        temp_node = temp_list_2.pop()
                        res_temp_list.append(temp_node.val)
                        if temp_node.left is not None:
                            temp_list_1.append(temp_node.left)
                        if temp_node.right is not None:
                            temp_list_1.append(temp_node.right)
                else:
                    while len(temp_list_2) > 0:
                        temp_node = temp_list_2.pop()
                        res_temp_list.append(temp_node.val)
                        if temp_node.right is not None:
                            temp_list_1.append(temp_node.right)
                        if temp_node.left is not None:
                            temp_list_1.append(temp_node.left)
            # python的bool取反方式
            sign = bool(1 - sign)
            res_list.append(res_temp_list)
        return res_list


# 之字形打印二叉树
# 使用双栈和一个布尔标识符解决
# 注意：sign = True:  先压左子，再压右子；   sign = False: 先压右子，再压左子