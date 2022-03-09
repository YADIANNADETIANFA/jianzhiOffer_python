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
        temp_list_1 = list()
        temp_list_2 = list()
        temp_list_1.append(pRoot)
        while len(temp_list_1) > 0 or len(temp_list_2) > 0:
            res_temp_list = list()
            if len(temp_list_1) > 0:
                while len(temp_list_1) > 0:
                    temp_node = temp_list_1.pop(0)
                    res_temp_list.append(temp_node.val)
                    if temp_node.left is not None:
                        temp_list_2.append(temp_node.left)
                    if temp_node.right is not None:
                        temp_list_2.append(temp_node.right)
            else:
                while len(temp_list_2) > 0:
                    temp_node = temp_list_2.pop(0)
                    res_temp_list.append(temp_node.val)
                    if temp_node.left is not None:
                        temp_list_1.append(temp_node.left)
                    if temp_node.right is not None:
                        temp_list_1.append(temp_node.right)
            res_list.append(res_temp_list)
        return res_list


# 分行从上到下打印二叉树
# 使用两个列表解决