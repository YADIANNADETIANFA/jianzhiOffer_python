class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        result = False

        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False

        if pRoot1.val == pRoot2.val:
            result = self.HasSubtree(pRoot1.left, pRoot2.left) and self.HasSubtree(pRoot1.right, pRoot2.right)

        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)

        return result


# 树的子结构 （pRoot2是否为pRoot1的子结构，一部分）
