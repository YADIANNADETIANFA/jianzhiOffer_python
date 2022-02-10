class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def get_next(self, tree_node: TreeLinkNode):
        # 仅单个节点
        if tree_node.left is None and tree_node.right is None:
            return None
        if tree_node.right:
            res = tree_node.right
            while res.left:
                res = res.left
            return res
        elif tree_node == tree_node.parent.left:
            return tree_node.parent
        else:
            res = tree_node.parent
            while res == res.parent.right:
                res = res.parent.right
            if res.parent:
                return res.parent
            else:
                return None

# 二叉树的下一个节点
# 有右子节点，选右子，然后持续往左子走
# 无右子节点，是左子节点，选父节点
#           是右子节点，向上，直至找到其为左子，否则已为最后节点



