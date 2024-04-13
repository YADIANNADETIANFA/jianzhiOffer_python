class TreeLinkNode:
    def __init__(self, x):
        self.val = x,
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def getNext(self, pNode: TreeLinkNode) -> TreeLinkNode:
        if pNode is None:       # 输入为空
            return None
        if pNode.right:         # 有右子节点，选右子，然后持续往左子走
            pTmp = pNode.right
            while pTmp.left:
                pTmp = pTmp.left
            return pTmp
        elif pNode.next is None:        # 无右子节点，且为根
            return None
        elif pNode.next.left == pNode:  # 无右子节点，是左子节点，选父节点
            return pNode.next
        else:       # 无右子节点，是右子节点，向上，直至找到其为左子，否则已为最后节点
            while pNode.next is not None and pNode.next.right == pNode:
                pNode = pNode.next
            if pNode.next is not None and pNode.next.left == pNode:
                return pNode.next
            if pNode.next is None:
                return None
            return None


# 二叉树的下一个节点
# 有右子节点，选右子，然后持续往左子走
# 无右子节点，是左子节点，选父节点
#           是右子节点，向上，直至找到其为左子，否则已为最后节点
