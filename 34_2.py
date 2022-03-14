from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.temp = list()
        self.res = list()

    def FindPathCore(self, pNode: TreeNode, sum: int):
        sum -= pNode.val
        self.temp.append(pNode.val)

        if pNode.left is None and pNode.right is None:
            if sum == 0:
                # res中的各个元素会随着self.temp的变化而变化。即若{10,5,12,4,7},22，则最终结果为[[], []]
                # self.res.append(self.temp)

                my_list = list()
                for i in self.temp:
                    my_list.append(i)
                self.res.append(my_list)
        else:
            if pNode.left is not None:
                self.FindPathCore(pNode.left, sum)
            if pNode.right is not None:
                self.FindPathCore(pNode.right, sum)

        # dfs时记得弹出
        self.temp.pop()

    def FindPath(self, root: TreeNode, target: int) -> List[List[int]]:
        if root is None or target is None:
            return None
        self.FindPathCore(root, target)
        return self.res


if __name__ == '__main__':
    treeNode_1 = TreeNode(10)
    treeNode_2 = TreeNode(5)
    treeNode_3 = TreeNode(12)
    treeNode_4 = TreeNode(4)
    treeNode_5 = TreeNode(7)

    treeNode_1.left = treeNode_2
    treeNode_1.right = treeNode_3
    treeNode_2.left = treeNode_4
    treeNode_2.right = treeNode_5

    solution = Solution()
    res = solution.FindPath(treeNode_1, 22)
    print(res)


# 二叉树中和为某一值得路径（牛客二）
# 各节点的值可正可负可零
# 各路径必从根节点开始，必从叶子节点结束
