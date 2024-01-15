###引入需求

###定义一个函数，模拟学生调用之后的自我介绍

###介绍的时候需要说的信息是：大家好，我是xxx,来自xxxx,很高兴认识大家


# def print_myself(name,school_name,class_name):
#     """
#     模拟自我介绍
#     :return:
#     """
#     print("我是%s,来自%s学校%s班级，很高兴认识大家"%(name,school_name,class_name))
#
# print_myself("wanghao","shanghai","111")


def print_myself(name, school_name="hahhah", class_name="101"):
    """
    模拟自我介绍
    :return:
    """
    print("我是%s,来自%s学校%s班级，很高兴认识大家" % (name, school_name, class_name))


print_myself("wanghao", "shanghai", "111")
