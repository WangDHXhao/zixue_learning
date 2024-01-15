#break在哪个循环中就结束哪一个

i = 0
while i < 5:
    print("-" * 30)
    i += 1
    #break  #本次break会结束外层循环
    j = 0
    while j < 3:
        print("j=%d" % j)
        break  # 本次break会结束内层循环
        j += 1
