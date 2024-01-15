"""
能否广播必须从axis的最大值向最小值看去，
依次对比两个要进行运算的数组的axis的数据宽度是否相等，
如果在某一个axis下(axis=1时横看，列相同)，一个数据宽度为1，另一个数据宽度不为1，
那么numpy就可以进行广播；
但是一旦出现了在某个axis下两个数据宽度不相等，
并且两者全不为1的状况，就无法广播。
"""

import numpy as np

a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([0, 1, 2, 3])
print(a + b)
# ValueError: operands could not be broadcast together with shapes (4,3) (4,)
