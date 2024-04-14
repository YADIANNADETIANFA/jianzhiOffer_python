class Solution:
    # 调整数组顺序，使奇数位于偶数前面，奇数之间和偶数之间相对位置不做要求
    def reOrderArrayTwo(self, array: list[int]) -> list[int]:
        # 头尾双指针
        left, right = 0, len(array) - 1
        while left < right:
            # 跳过左边的奇数
            while left < right and array[left] % 2 == 1:
                left += 1
            # 跳过右边的偶数
            while left < right and array[right] % 2 == 0:
                right -= 1
            # 满足条件，交换
            while left < right and array[left] % 2 == 0 and array[right] % 2 == 1:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return array

    # 同上，但要求奇数之间和偶数之间相对位置不变
    def reOrderArray(self, array: list[int]) -> list[int]:
        if len(array) <= 1:
            return array
        array_single, array_double = [], []
        for item in array:
            if item % 2 == 1:
                array_single.append(item)
            else:
                array_double.append(item)
        return array_single + array_double


# 调整数组顺序使奇数位于偶数前面(一)
