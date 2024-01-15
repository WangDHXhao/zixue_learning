# -*- coding: UTF-8 -*-
''' 
@File    ：Stack.py
@IDE     ：PyCharm 
@Author  ：Wangzyhao
@Date    ：2023/11/22 14:04 
'''


class Test():
    def test(self):
        stack = []


        stack.append(1)
        stack.append(2)
        stack.append(3)
        print(stack)

        stack[-1]
        temp = stack.pop()
        print(temp)


        print(stack)

        print(stack==0)


        while(len(stack) > 0):
            temp = stack.pop()
            print(temp)


if __name__ == '__main__':
    test = Test()
    test.test()
