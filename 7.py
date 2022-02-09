class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, vin) -> TreeNode:
        if len(pre) > 0:
            root = TreeNode(pre[0])
            root_index = vin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:1+root_index], vin[:root_index])
            root.right = self.reConstructBinaryTree(pre[1+root_index:], vin[root_index+1:])
            return root

# 重建二叉树
# 递归