class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, pRoot: TreeNode) -> TreeNode:
        # 递归
        # if pRoot is None:
        #     return None
        #
        # pTemp = pRoot.left
        # pRoot.left = pRoot.right
        # pRoot.right = pTemp
        # self.Mirror(pRoot.left)
        # self.Mirror(pRoot.right)
        #
        # return pRoot

        # 迭代
        if pRoot is None:
            return None

        my_list = []
        my_list.append(pRoot)

        while len(my_list) > 0:
            pNode = my_list.pop(0)  # 弹出并返回首个元素
            pTemp = pNode.left
            pNode.left = pNode.right
            pNode.right = pTemp

            if pNode.left is not None:
                my_list.append(pNode.left)
            if pNode.right is not None:
                my_list.append(pNode.right)

        return pRoot


# 二叉树镜像
