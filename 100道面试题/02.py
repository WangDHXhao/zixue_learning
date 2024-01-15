"""
求某数的阶乘

"""


def get_jiecheng(number):
    # # result = 1
    # # for i in range(1, number+1):    ###自己的方法
    # #     result *= i
    # return result

    result = 1
    while number > 0:
        result *= number
        number -= 1

    return result


print("阶乘3=", get_jiecheng(3))
print("阶乘6=", get_jiecheng(6))
print("阶乘100=", get_jiecheng(100))



"""

学会了如何设置断点来debug内容

"""