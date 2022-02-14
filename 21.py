class Solution:

    # 调整数组顺序，使奇数位于偶数前面，奇数之间和偶数之间相对位置不做要求
    def reOrderArrayTwo(self, array):
        # 头尾双指针
        left = 0
        right = len(array) - 1
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
    # 遍历数组，分别挑出奇数偶数后合并，时间复杂度O(n)，空间复杂度O(n)
    def reOrderArray(self, array):
        if len(array) <= 1:
            return array
        array_single = []
        array_double = []
        for i in array:
            if i % 2 == 1:
                array_single.append(i)
            else:
                array_double.append(i)
        return array_single + array_double

    # 在原基础数组上进行修改：遍历数组，找到一个奇数就把这个奇数前移。需记录当前有多少个奇数，如果当前有k个奇数，那么接下来找到的奇数
    # 原本在array[i]则需挪到array[k]，而array[k] ~ array[i - 1]需要依次后移一位
    # 时间复杂度O(n^2)，空间复杂度O(1)，不建议，参考自牛客网
    def reOrderArray_2(self, array):
        if len(array) <= 1:
            return array
        k = 0
        for i in range(0, len(array)):
            if array[i] % 2 == 1:
                c = array[i]
                # 倒序，参数start大于end，步长-1，仍[start, end)
                # range(5, 0, -1): 5 4 3 2 1
                for j in range(i-1, k-1, -1):
                    array[j+1] = array[j]
                array[k] = c
                k += 1
        return array





