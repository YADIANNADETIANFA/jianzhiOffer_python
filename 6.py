class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode: ListNode) -> list[int]:
        res = []
        while listNode is not None:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]


# 从尾到头打印链表

# Python中[:-1]与[::-1]的区别
# a = [0,1,2,3,4,5,6,7,8,9]
# b = a[i:j] 表示取a[i]到a[j-1]
# i缺省默认为0；j缺省默认为len(a);因此a[:]为取全部
# b = a[i:j:s]，s为步长，缺省为1
# 当s < 0时，i缺省值为-1，j缺省值为-len(a) - 1
# 所以a[::-1]相当于a[-1 : -len(a) - 1 : -1]，即倒序
# 从后往前数，最后一个位置为-1，倒数第二个位置为-2
# 因此a[:-1]表从位置0到位置-1之前的数，即除最末尾后的所有数

# https://www.cnblogs.com/mxh1099/p/5804064.html
