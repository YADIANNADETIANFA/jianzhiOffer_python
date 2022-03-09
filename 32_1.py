from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintFromTopToBottom(self, root: TreeNode) -> List[int]:
        res_list = list()
        if root is None:
            return res_list
        temp_list = list()
        temp_list.append(root)
        while len(temp_list) > 0:
            res_list.append(temp_list[0].val)
            temp_node = temp_list.pop(0)
            if temp_node.left is not None:
                temp_list.append(temp_node.left)
            if temp_node.right is not None:
                temp_list.append(temp_node.right)
        return res_list


if __name__ == '__main__':
    solution = Solution()
    treeNode = TreeNode(1)
    res = solution.PrintFromTopToBottom(treeNode)


# 从上到下打印二叉树（不分行）
# 一个列表解决