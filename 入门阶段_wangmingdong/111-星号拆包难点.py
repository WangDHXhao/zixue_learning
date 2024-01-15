# def test1(*args,**kwargs):
#     print("------在test1函数中-------")
#     print("args:",args)
#     print("kwargs",kwargs)
#
#
# def test2(*args,**kwargs):
#     print("------在test2函数中-------")
#     print("args:", args)
#     print("kwargs", kwargs)
#     test1(args,kwargs)
#
# test2(11,22,33,name="wanglaoshi",age=18)


# 若也想test2中接收的参数原封不动传到test1中则


def test1(*args, **kwargs):
    print("------在test1函数中-------")
    print("args:", args)
    print("kwargs", kwargs)


def test2(*args, **kwargs):
    print("------在test2函数中-------")
    print("args:", args)
    print("kwargs", kwargs)
    test1(*args, **kwargs)  # 对其进行拆包，字典拆包后就是 key = value
    # test1(args,kwargs)


test2(11, 22, 33, name="wanglaoshi", age=18)
