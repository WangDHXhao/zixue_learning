
"""
具体需求看img内的图片


设计带有私有成员的手机类，内容包括：

（1）私有成员变量：__is_5g_enable,
类型bool，True表示开启5g，False表示关闭5g
（2）私有成员方法。。。。。。。。


"""


class Phone():

    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable>0:
            print("5g已开启")
        else:
            print("5g关闭，使用4g网络")


    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")



phone=Phone()
phone.call_by_5g()

