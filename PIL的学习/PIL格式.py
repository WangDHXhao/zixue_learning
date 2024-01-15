"""
测试PIL库的数据格式，

Python Pillow(PIL)库的用法介绍

Pillow库是一个Python的第三方库。

在Python2中，PIL(Python Imaging Library)是一个非常好用的图像处理库，但PIL不支持Python3，所以有人(Alex Clark和Contributors)提供了Pillow，可以在Python3中使用。

以及对图片的一些操作变化

"""

import numpy as np
from PIL import Image

image=Image.open('../img/R7FQW$O}SNR1LGC)}E0PP`8.png')
#img.show()
from PIL import Image

print('width: ', image.width)
print('height: ', image.height)
print('size: ', image.size)
print('mode: ', image.mode)
print('format: ', image.format)
#print('is_animated: ', image.is_animated)
print('readonly: ', image.readonly)
print('info: ', image.info)





"""

width:  929
height:  398
size:  (929, 398)
mode:  RGB
format:  PNG
readonly:  1
info:  {}


width属性表示图片的像素宽度，height属性表示图片的像素高度，width和height组成了size属性，size是一个元组。

mode属性表示图片的模式，如RGBA，RGB，P，L等。

format属性表示图片的格式，格式一般与图片的后缀扩展名相关。

readonly属性表述图片是否为只读，值为1或0，表示的是布尔值。

info属性表示图片的信息，是一个字典。

"""



