# a = int(input('请输入一个数：'))
# print('这个数的类型是',type(a))
# print(type(a))
#
#
# list1 = ["这", "是", "一个", "测试"]
# for i in range (len(list1)):
#     print(i ,list1[i])
#
#
# list1 = ["这", "是", "一个", "测试"]
# for index, item in enumerate(list1):
#     print(index, item)
#
#
# print('a')
#
#

import torch
import torch.nn as nn
import numpy as np

# x = torch.randn(4,5)
# m = nn.Dropout(p=0.5)
# x = m(x)
# print(x)

# x = torch.tensor([1, 2, 3, 4])
# y = torch.unsqueeze(x, 0)
# print(y)
# z = torch.unsqueeze(x, 1)
# print(z)


# x = torch.zeros(3,4)
# print(x)

#
# x = torch.ones(5, 5)
#
# print(x)
#
# y = np.ones((5, 5))
# print(y)
#


#
# x = torch.randn(4,4)
#
#
# print(x.size())
#
#
# y = x.view(16)
#
# print(y.size())


nums1 = [6, 7, 8, 9]
nums2 = [6, 7, 8, 9]
for i in nums1:
    index = nums2.index(i)
    print(index)
