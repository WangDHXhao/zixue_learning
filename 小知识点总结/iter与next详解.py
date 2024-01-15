

"""
列表和迭代器区别

列表不论遍历多少次，表头位置始终是第一个元素；

迭代器遍历结束后，不再指向原来的表头位置，而是为最后元素的下一个位置


"""

a= [1, 2, 3]
a_iter = iter(a)
print(a_iter)
print(next(a_iter))
print(next(a_iter))
