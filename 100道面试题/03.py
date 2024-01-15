"""
求圆的面积

"""

import math

def com_area_of_circle(r):
    return round(math.pi*r*r,2)


print("area of 2 is: ",com_area_of_circle(2))
print("area of 4 is: ",com_area_of_circle(4))

print("area of 3.14 is: ",com_area_of_circle(3.14))


"""
学到了如何保留两位小数的函数round（）

"""