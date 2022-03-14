class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.res = 0

    # 错误思路!
    # def FindPathCore(self, pNode: TreeNode, sum: int):
    #     sum -= pNode.val
    #     if sum == 0:
    #         self.res += 1
    #     if pNode.left is not None:
    #         self.FindPathCore(pNode.left, sum)
    #         self.FindPathCore(pNode.left, sum + pNode.val)
    #     if pNode.right is not None:
    #         self.FindPathCore(pNode.right, sum)
    #         self.FindPathCore(pNode.right, sum + pNode.val)
    #
    # def FindPath(self, root: TreeNode, sum: int) -> int:
    #     if root is None or sum is None:
    #         return 0
    #     self.FindPathCore(root, sum)
    #     return self.res

    def dfs(self, pNode: TreeNode, sum: int):
        sum -= pNode.val
        if sum == 0:
            self.res += 1
        if pNode.left is not None:
            self.dfs(pNode.left, sum)
        if pNode.right is not None:
            self.dfs(pNode.right, sum)

    def FindPath(self, root: TreeNode, sum: int) -> int:
        if root is None or sum is None:
            return 0
        # 重点在这里！这里是dfs！
        self.dfs(root, sum)
        if root.left is not None:
            # 重点在这里！这里是FindPath！
            self.FindPath(root.left, sum)
        if root .right is not None:
            # 重点在这里！这里是FindPath！
            self.FindPath(root.right, sum)
        return self.res


if __name__ == '__main__':
    # eg_1
    # treeNode_1 = TreeNode(1)
    # treeNode_2 = TreeNode(2)
    # treeNode_3 = TreeNode(3)
    # treeNode_4 = TreeNode(4)
    # treeNode_5 = TreeNode(5)
    #
    # treeNode_1.right = treeNode_2
    # treeNode_2.right = treeNode_3
    # treeNode_3.right = treeNode_4
    # treeNode_4.right = treeNode_5
    # solution = Solution()
    # res = solution.FindPath(treeNode_1, 3)
    # print(res)

    # eg_2
    treeNode_1 = TreeNode(1)
    treeNode_2 = TreeNode(2)
    treeNode_3 = TreeNode(3)
    treeNode_4 = TreeNode(4)
    treeNode_5 = TreeNode(5)
    treeNode_4_2 = TreeNode(4)
    treeNode_3_2 = TreeNode(3)
    treeNode_m1 = TreeNode(-1)

    treeNode_1.left = treeNode_2
    treeNode_1.right = treeNode_3
    treeNode_2.left = treeNode_4
    treeNode_2.right = treeNode_5
    treeNode_3.left = treeNode_4
    treeNode_3.right = treeNode_3_2
    treeNode_5.left = treeNode_m1
    solution = Solution()
    res = solution.FindPath(treeNode_1, 6)
    print(res)


# 二叉树中和为某一值得路径（牛客三）
# 各节点的值可正可负可零
# 该题路径定义不需要从根节点开始，也不需要在叶子节点结束
