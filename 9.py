tmp_list = [1, 2, 3, 4, 5, 6]

print(tmp_list.pop(0))  # 取出，删除，并返回index处的元素。若省略index则默认处理最末尾元素
tmp_list.append(7)
print(tmp_list)


# 用两个栈实现队列
# 无需脱裤子放屁，直接用列表append和pop
