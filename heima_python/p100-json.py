"""
1.什么是JSON？？？

json是一种轻量级的数据交互格式。

本质是一个带有特定格式的字符串


2.主要功能：

json就是一种在各个编程语言中流通的数据格式，

负责不同编程语言中的数据传递和交互，类似于：

国际通用语言：英语

中国56个名族不同地区的通用语言：普通话


3.json的数据格式可以是python中的字典、列表（里面嵌套字典）形式


"""

###python数据和json数据的相互转换

import json

data = [{'name': "老王", 'age': 16}, {'name': "张三", 'age': 20}]



json_str = json.dumps(data,ensure_ascii=False)     #通过json.dumps()将python数据转换为json数据

print(type(json_str))
print(json_str)


#data = json.loads(data)    #通过json.loads()将json数据转换为python数据
