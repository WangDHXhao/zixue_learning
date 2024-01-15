"""
不定长参数：就是传递实参个数是可以任意的
在python中不定长参数有两种方式
*args 这种方式能够存储多余的实参
"""


# def sum_nums(a, b, *args):
#     """
#
#     :param a:
#     :param b:
#     :param args:
#     :return:
#     """
#     sum_result = a + b
#     print("结果是：%d" % sum_result)
#     print("args=",args,type(args))
#
#
# # sum_nums(1, 2)
# sum_nums(1, 2, 3)
# # sum_nums(1, 2, 3, 4)


def sum_nums(a, b, *args):
    """

    :param a:
    :param b:
    :param args:
    :return:
    """
    sum_result = a + b
    for t in args:
        sum_result += t

    print("结果是：%d" % sum_result)


sum_nums(1, 2)
sum_nums(1, 2, 3)
sum_nums(1, 2, 3, 4)
sum_nums(1, 2, 3, 4, 5)
