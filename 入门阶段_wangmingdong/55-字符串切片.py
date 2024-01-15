# 字符串切片就是从原本的字符中提取一部分字符

# demo1

name = "abcdef"
print(name[0:3])  # 类似range的用法

# demo2
name1 = "abcdef"
print(name1[:3])  # 如果只有一个冒号：且左边没有任何数字，那么默认为0

# demo3
name2 = "abcdef"
print(name2[3:5])  # 左取右不取

# demo4
name3 = "abcdef"
print(name3[2:])  # 如果只有一个冒号：且右侧没有任何数字，那么就相当于最后一个（包括最后一个）

# demo4
name3 = "abcdef"
print(name3[2:-1])  # 下标从左往右是0、1、2。。。从右往左是-1、-2、-3.。。

# demo5

name5 = "abcdef"
print(name5[1:-1])  # 输出bcde

# demo6

name6 = "abcdef"
print(name6[1:5:2])  # 输出bd

# demo9

name9 = "abcdef"
print(name6[::1])  # 输出abcdef
print(name6[::-1])  # fedcba
# 如果有两个冒号：且第一个冒号左边没有数字，第二个冒号也没有数字
##那么就默认从一侧取到另一侧


# demo10

name10 = "abcdef"
print(name10[::])  # 输出abcdef
print(name10[:])   # 输出abcdef