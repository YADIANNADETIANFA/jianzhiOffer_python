class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        if pRoot2 is None:
            return False
        if pRoot1 is None:
            return False

        if pRoot1.val == pRoot2.val:
            if self.HasSubtreeCore(pRoot1.left, pRoot2.left) and self.HasSubtreeCore(pRoot1.right, pRoot2.right):
                return True     # Core通过，很好，结果为True；Core不通过，也无所谓，下面从头开始

        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def HasSubtreeCore(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.HasSubtreeCore(pRoot1.left, pRoot2.left) and self.HasSubtreeCore(pRoot1.right, pRoot2.right)
        else:
            return False


# 树的子结构 (pRoot2是否为pRoot1的子结构，一部分)
