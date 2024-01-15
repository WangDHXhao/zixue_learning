"""

和文件相关的类定义

"""

###定义一个抽象类用来做顶层设计，确定有哪些功能

from data_define import Record


class FileReader(object):
    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record对象，
        将他们都封装到list内返回即可"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 完成成员变量记录文件的路径

    ###复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        for