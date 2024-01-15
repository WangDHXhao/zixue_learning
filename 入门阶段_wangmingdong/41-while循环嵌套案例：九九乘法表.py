i = 1

while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (i, j, i * j), end="")  #print,默认会换行，end=""是强制不换行
        j += 1
    print("\n")
    i += 1
