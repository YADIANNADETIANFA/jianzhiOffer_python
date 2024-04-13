class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, preOrder: list[int], vinOrder: list[int]) -> TreeNode:
        if len(preOrder) > 0:
            root = TreeNode(preOrder[0])
            root_index = vinOrder.index(preOrder[0])
            root.left = self.reConstructBinaryTree(preOrder=preOrder[1:1+root_index], vinOrder=vinOrder[:root_index])
            root.right = self.reConstructBinaryTree(preOrder=preOrder[1+root_index:], vinOrder=vinOrder[1+root_index:])
            return root
        else:
            return None


# 根据前序遍历和中序遍历，重建二叉树
# 递归解法
