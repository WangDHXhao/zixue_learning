def test(a,b,*args,**kwargs): ###只要有一个*就是存多余参数，
    print(a)            ####两个**就是存命名参数不一定叫args，kwargs（默认是）
    print(b)
    print(args)
    print(kwargs)

# test(11,22)
#test(11,22,33)
test(11,22,33,c=33)

test(11,22,33,44)