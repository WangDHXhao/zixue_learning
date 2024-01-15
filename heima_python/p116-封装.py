### 定义一个类，内含有私有成员变量和私有成员方法


class Phone():

    __current_voltage = 0.5  # 定义私有成员，不管是变量还是方法，都是以__开头

    def __keep_single_core(self):   #还是方法
        print("让cpu以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >=1:
            print("5g通话已开启")
        else:
            print("电量不足，无法使用5g通话，并设置为单核运行进行省电")


phone=Phone()
#phone.__keep_single_core()   #AttributeError: 'Phone' object has no attribute '__keep_single_core'
phone.call_by_5g()

