class Solution:
    def duplicate(self, numbers: list[int]) -> int:
        tmp_set = set()
        for item in numbers:
            if item in tmp_set:
                return item
            else:
                tmp_set.add(item)
        return -1


# 数组中重复数字
