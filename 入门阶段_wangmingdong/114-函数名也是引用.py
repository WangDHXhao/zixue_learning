def test1():
    print("我是test1函数")
    return 100

num = test1  #没有（）也并没有报错，说明成立，
            #则函数也是引用，test1指向某个地址，地址中存放了函数内的代码
print(num)

print(test1)


test1=[11,22]

print(test1)

