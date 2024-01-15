# -*- coding: UTF-8 -*-
''' 
@File    ：random_seed.py
@IDE     ：PyCharm 
@Author  ：Wangzyhao
@Date    ：2024/1/15 9:25 
'''

import random

print("第一次随机生成")
print(random.randint(1, 100))
print(random.randint(1, 100))


print("第二次随机生成")
print(random.randint(1, 100))
print(random.randint(1, 100))


random.seed(11)
print("第一次设定了种子后的随机生成")
print(random.randint(1, 100))
print(random.randint(1, 100))



random.seed(11)
print("第二次设定了种子后的随机生成")
print(random.randint(1, 100))
print(random.randint(1, 100))