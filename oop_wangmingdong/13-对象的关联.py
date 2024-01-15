class ClassRoom(object):
    def __init__(self, name):  # 在一个类中添加一个属性
        self.name = name
    def add_student(self,new_student):
        self.student=new_student

class Student(object):
    def __init__(self, name):
        self.name = name


class205 = ClassRoom("205班")
stu1 = Student("学生1")


###直接通过对象名.属性名=另外一个对象名，让一个对象中的属性执行另外一个对象，
# ##此时他们直接有了关系
class205.student = stu1


###也可以通过定义一个方法，然后调用这个方法的时候将另外一个对象引用当作实参

###既然已经让两个对象有了关系，那么怎么取用呢？？？

class205.student.name  #此时name是什么？？？学生1

class205.name      ##205班

stu1.name       ###学生1

print(class205.student.name )