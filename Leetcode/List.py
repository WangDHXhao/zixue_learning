# -*- coding: UTF-8 -*-
''' 
@File    ：List.py
@IDE     ：PyCharm 
@Author  ：Wangzyhao
@Date    ：2023/11/22 13:32 
'''

a = [1, 2, 3, 45, 6]
size = len(a)
print(size)
"""
# 删除元素
a.remove(1)  ###括号内是元素
print(a)
a.pop(1)  ###括号内是索引
print(a)

a.pop()  ###不写则默认是删除最后一个
print(a)

b = [7, 8, 9, 10, 11, 12]
"""

"""
###遍历数组（3种方法）
for i in b:
    print(i)
for index, element in enumerate(b):
    print("Index at ", index, "is : ", element)
for i in range(0, len(b)):
    print("i :", i, "element", b[i])
"""

##查找某个元素

index = a.index(2)
print(index)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.reverse()
print(a)