"""
多态指：多种状态，即完成某个行为时，使用不同的对象会得到不同状态


同样的行为（函数），传入不同的对象，得到不同的状态

"""


class Animal(object):
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):  # 类型注解
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)  # 每个子类都继承了父类
make_noise(cat)

"""
抽象类就好比定义一个标准
包含了一些抽象的方法，要求子类必须实现

"""


class AC(object):
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):

    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea = Midea_AC()   #构建两个子类对象
gree = GREE_AC()

make_cool(midea)
make_cool(gree)

