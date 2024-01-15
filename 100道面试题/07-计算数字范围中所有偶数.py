def print_oushu(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result


begin = 4
end = 15

print(print_oushu(3, 15))

"""
用列表推导式更简单
[变量 for循环 判断式]
"""

data = [i for i in range(begin, end + 1) if i % 2 == 0]

print(data)
