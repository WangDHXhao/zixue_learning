# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序完成随机分配

# 分析：
# 1.定义一个列表，里面嵌套三个空列表 offices=[[][][]]

# 2.定义另一个列表，存储8位老师的名字[aa,bb,cc,.......]

# 3.假如将aa添加到第一个办公室中，大体的逻辑是：office[0].append(aa)



# 模拟三个办公室
import random

offices=[[],[],[]]
#定义所有老师的名字
teacher_names=['aa','bb','cc','dd','ee','ff','gg','hh']
#遍历出所有老师的名字
for name in teacher_names:
    random_office_num=random.randint(0,2)
    offices[random_office_num].append(name)

#打印测试

print(offices)
