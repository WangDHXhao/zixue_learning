"""

常用的魔术方法


"""


class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    ### __str__ 魔术方法
    def __str__(self):   #不再输出内存地址，而是输出想要的字符串
        return f"Student类对象，name:{self.name},age:{self.age}"


stu=Student("周杰伦",31)

print(stu)

print(str(stu))
