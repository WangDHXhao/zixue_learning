"""

简要总结：

if __ name __ == ’ __ main __'的意思是：
1.当.py文件被直接运行时，
if __ name __== ’ __ main __'之下的代码块将被运行；
2.当.py文件以模块形式被导入时，
if __ _name __== ’ __ main __'之下的代码块不被运行。

"""

"""
那么if __ name __ == ’ __ main __’ 这句代码具体是怎么实现的呢

重点：：：
__name__ 是系统内置变量，用于表示当前模块的名字，即所在文件名
if name == ‘main’: 这句话的核心无非就是在判断该程序文件是否作为主程序入口。

如果直接运行该程序文件，该文件作为主程序入口，name == ‘main’ 主程序。
如果在运行主程序的时候调用其他程序文件，
其他程序入口name ！= ‘main’ 自然就不等于main主程序 。


"""

# # import my_module1
# #
# # my_module1.test(1,2)
#
#
#
# """
#
# 导入不同模块的同功能名
# 后面的导入会把前面的覆盖
#
# """
# from my_module1 import test
# from my_module2 import test
#
# test(1,2)


"""

如果一个模块文件中有“__all__”变量，
当使用“from XXX import *”时，
只能导入这个列表中的元素
(all只作用在*上)
"""

from my_module1 import *

test_a(1, 3)

