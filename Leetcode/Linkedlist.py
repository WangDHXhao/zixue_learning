# -*- coding: UTF-8 -*-
''' 
@File    ：Linkedlist.py
@IDE     ：PyCharm 
@Author  ：Wangzyhao
@Date    ：2023/11/22 13:46 
'''

from collections import *
linkedlist = deque()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)


"""

操作类似于列表

"""

print(linkedlist)
print(type(linkedlist))


linkedlist.insert(2,99)
print(linkedlist)


element = linkedlist[2]
print(element)


index = linkedlist.index(99)
print(index)

linkedlist[2] = 88
print(linkedlist)

linkedlist.remove(88)
print(linkedlist)


length = len(linkedlist)
print(length)