class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res_list = list()

    def Convert(self, pRootOfTree: TreeNode):
        if pRootOfTree is None:
            return None
        self.MidTravel(pRootOfTree)
        for index, node in enumerate(self.res_list[:-1]):
            node.right = self.res_list[index + 1]
            self.res_list[index + 1].left = node
        return self.res_list[0]

    def MidTravel(self, pNode: TreeNode):
        if pNode is None:
            return
        self.MidTravel(pNode.left)
        self.res_list.append(pNode)
        self.MidTravel(pNode.right)


# 二叉搜索树与双向链表

# 先中序遍历，将所有节点保存到一个list，
# 然后对这个list[:-1]进行遍历，构成双向链表

# line = 'abcde'
# line[:-1]     'abcd'      就是去除这行文本的最后一个字符后，剩余的部分
# line[::-1]    'edcba'


# 枚举，i为索引，j为值
# line = [1, 2, 3, 4, 5]
# for i, j in enumerate(line):
#   print(i, j)
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
