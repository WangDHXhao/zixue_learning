"""

1.模块的导入

"""
# import time
#
# print("你好吗")
#
# time.sleep(10)    ##通过使用模块内的类、函数、变量
#
# print("我好")


"""
2.使用from 导入 time 的sleep功能（函数）
"""

# from time import sleep   ##只用sleep这个功能
# print("我好")
# sleep(5)
# print("你好吗")


"""
3.使用 * 导入time 模块的全部内容

"""

# from time import *
# print("你好吗")
# sleep(5)    ####与方法1进行对比，同样是将time模块的内容全部导入，但是用的时候不需要写time.sleep()
# print("我好")


"""

4.as定义别名

"""

# import time as t

from time import sleep as sl

print("你好吗")
sl(5)
print("我好")
