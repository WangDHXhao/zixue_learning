# 作用：结束本次循环

i = 1
while i <= 5:
    print("---------")
    i += 1
    continue    #continue 会让本次循环中剩下的代码不会执行
    print("i=%d" % i)

