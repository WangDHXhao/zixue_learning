class MacBookPro(object):
    def __init__(self, cpu="i10", memory=32):  # 魔法方法   2.自动调用__init__方法，且self指向刚刚创建的对象
        """__init__方法一般情况下都是对刚刚创建成功的对象进行初始化
        设置一些默认的数据

        """
        self.cpu = cpu
        self.memory = memory

    def print_info(self):
        print("当前电脑的配置是：", self.cpu, self.memory)


###创建一个苹果笔记本电脑对象
my_mac_book = MacBookPro()  # 1.创建对象
# my_mac_book.set_pro()   #如何不写这一行而直接调用
my_mac_book.print_info()

my_mac_book2 = MacBookPro("i11",64)
my_mac_book2.print_info()
