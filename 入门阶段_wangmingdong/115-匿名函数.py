###之前用def定义函数，就是普通的函数，它适合用来编写完整的功能代码


def xxx():
    pass


####匿名函数,是一个没有名字的函数，它的定义方式很独特，并没有def


# lambda  形参1，形参2，形参3.。。。   ：表达式

lambda a, b: a + b
# 因为无名，那改如何调用



#一般情况下：我们先定义一个变量，然后用变量名指向匿名函数

#1.先定义变量指向匿名函数

my_test_func=lambda a, b: a + b

#2.通过变量名（）调用

num = my_test_func(11,22)

print(num)

#还有一种方式：将匿名函数当作实参

def fun(a,b,opt):
    print("a=%d"%a)
    print("b=%d" % b)
    print("result=%d" % opt(a,b))

fun(1,2,lambda x,y:x+y)

