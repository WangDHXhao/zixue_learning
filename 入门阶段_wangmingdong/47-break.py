# break 的作用是结束整个循环（无论是for还是while循环）

#1.在while中的使用
# i = 1
# print("woshiceshi....111")
# while i <= 5:
#     if i >= 3:
#         break
#     print("i=%d" % i)
#     i += 1
# print("woshiceshi....222")



#2.在while中的使用
for i in range(10):
    print("i=%d" % i)
    break
    