from typing import List


class Solution:
    def IsPopOrder(self, pushV: List[int], popV: List[int]) -> bool:
        if pushV is None or popV is None:
            return False
        if len(pushV) != len(popV):
            return False

        my_list = list()
        index_push = 0
        index_pop = 0

        while index_push < len(pushV) and index_pop < len(popV):
            while index_push < len(pushV) and (len(my_list) == 0 or my_list[-1] != popV[index_pop]):
                my_list.append(pushV[index_push])
                index_push += 1
            if my_list[-1] != popV[index_pop]:
                # pushV已将所有数据都压入my_list了，但还是没有能弹出的数据
                return False

            while len(my_list) != 0 and my_list[-1] == popV[index_pop]:
                # 弹出可弹出的数据
                index_pop += 1
                my_list.pop()

        # 这里必须要加个判断，否则[1,2,3,4,5],[4,3,5,1,2]不过
        if len(my_list) > 0:
            return False
        else:
            return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.IsPopOrder([1, 2, 3, 4, 5,4,7], [4, 7,5,4,3, 2, 1]))


# 栈的压入，弹出序列     （假设压入栈的所有数字均不相等！）
# 使用辅助栈

# 若压入栈的数字可相等，比如[1, 2, 3, 4, 5, 4, 7], [4, 7, 5, 4, 3, 2, 1]，会被误判为False
# 若题目允许压入数字相等，我们可以手动改变压入的数字值，使每个值变得不相等，然后再用老方法解题
# 上例可手动改为[1_1, 2_1, 3_1, 4_1, 5_1, 4_2, 7_1], [4_2, 7_1, 5_1, 4_1, 3_1, 2_1, 1_1], _2表示第二次出现该数字     但若弹出数组不给出_2这种数字出现次数，那就不好搞了。。