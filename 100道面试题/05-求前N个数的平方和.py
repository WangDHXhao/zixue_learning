"""

求N个数字的平方和

"""
def ping_fang_he(num):
    res = 0
    for i in range(1,num+1):
        res+=i**2
    return res



print(ping_fang_he(3))
print(ping_fang_he(4))
print(ping_fang_he(6))
