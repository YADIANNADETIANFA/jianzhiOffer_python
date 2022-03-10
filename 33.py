from typing import List


class Solution:

    def verifyCore(self, beginIndex: int, endIndex: int, sign: bool, root: int) -> bool:
        if sign:
            # 左子树
            for i in range(beginIndex, endIndex + 1, 1):
                if self.my_list[i] > root:
                    return False
        else:
            # 右子树
            for i in range(beginIndex, endIndex + 1, 1):
                if self.my_list[i] < root:
                    return False

        # 无节点或仅一个节点
        if beginIndex >= endIndex:
            return True
        p_root = self.my_list[endIndex]
        index = beginIndex
        while self.my_list[index] < p_root:
            index += 1
        return self.verifyCore(beginIndex, index - 1, True, p_root) and self.verifyCore(index, endIndex - 1, False, p_root)

    def VerifySquenceOfBST(self, sequence: List[int]) -> bool:
        # 这两个特殊情况True或False都行，根据题目要求来
        if sequence is None or len(sequence) == 0:
            return False
        # 长度1或2，必True
        if len(sequence) < 3:
            return True

        self.my_list = sequence
        p_root = sequence[-1]
        index = 0
        while sequence[index] < p_root:
            index += 1
        return self.verifyCore(0, index - 1, True, p_root) and self.verifyCore(index, len(sequence) - 2, False, p_root)


if __name__ == '__main__':
    solution = Solution()
    print(solution.VerifySquenceOfBST([5, 7, 6, 9, 11, 10, 8]))


# 二叉搜索树的后序遍历序列

# 后序遍历： 左子树，右子树，根

# 二叉搜索树，可能为空；一颗非空的二叉搜索树满足：
#   1、根节点的左子树中，元素的关键点（如果有的话）都小于根节点关键字
#   2、      右                             大
#   3、根节点的左右子树也都是二叉搜索树
#   （没有等于，只有小于或大于；若运行等于，那是“有重复值的二叉搜索树”）

# 判是否左子全都小于根，右子全都大于根，不是则False，是就递归左子、右子树
# return (left and right)