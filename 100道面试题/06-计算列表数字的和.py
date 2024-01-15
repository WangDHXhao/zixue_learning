def sum_of_list(param_list):
    t = 0
    for i in param_list:
        t += i
    return t


list1 = [1, 2, 3, 4]
list2 = [17, 3, 5, 5]

print(sum_of_list(list1))
print(sum_of_list(list2))


"""

也可使用python内置函数

"""
print(sum(list1))
print(sum(list2))
