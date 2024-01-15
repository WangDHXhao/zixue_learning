# -*- coding: UTF-8 -*-
''' 
@File    ：Queue.py
@IDE     ：PyCharm 
@Author  ：Wangzyhao
@Date    ：2023/11/22 13:56 
'''


from collections import *

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(type(queue))


# temp1 = queue[0]
# print(temp1)
#
# temp2 = queue.popleft()
# print(temp2)
#
# print(len(queue)==0)

while (len(queue) != 0):
    temp = queue.popleft()
    print(temp)
