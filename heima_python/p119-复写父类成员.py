"""


对哪个方法不满意，即可重新写


"""


class Phone(object):
    IMEI = None
    producer = "ITdark"

    def call_by_5g(self):
        print("使用5g网络进行通话")


class My_phone(Phone):
    producer = "itheima"

    def call_by_5g(self):
        print("开启单核模式，确保通话的时候省电")
        # # print("使用5g网络进行通话")  #父类中已有不用再写，直接调用
        # ###方式1
        # print(f"父类的厂商是{Phone.producer}")
        # Phone.call_by_5g(self)

        ###方式2
        print(f"父类的厂商是{super().producer}")   ###调用父类的
        super().call_by_5g()
        print("关闭cpu单核模式，确保性能")

"""
多继承情况下，
如果出现同名成员，使用super()方式2调用父类成员时，
优先匹配先继承的父类成员

"""





phone = My_phone()


phone.call_by_5g()


print(phone.producer)