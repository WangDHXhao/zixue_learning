"""
1.PIL数据读取格式

"""
import numpy as np
from PIL import Image

img = Image.open('../img/R7FQW$O}SNR1LGC)}E0PP`8.png')
img = np.array(img)  # img是数值范围在0-255之间的uint8格式数组

print(img)
# # 注意img的形状是 H x W x C
# # 如果想改变数组形状，可以使用transpose(idx1, idx2, idx3)
#
#
# """
# 2.转换为tensor形式
#
#
# """
#
# ####在Pytorch中，图片张量形式是 C x H x W，所以要把数组转置转置，用到transpose
#
# import torch
# from torchvision import transforms
#
# # 1.
# img = np.array(img).transpose(2, 0, 1)  # 表示成C*H*W形式
#
# img1 = torch.tensor(img / 255)  # 神经网络中的张量数值一般在0~1之间归一化处理，所以除以255
# # 此时获得的数组就是形状为C x H x W的张量，数值0-1
#
# # 2.
# # 或者经过transforms处理
#
# trans = transforms.Compose([
#     transforms.ToTensor()
# ])
# img2 = trans(img)
#
# # print(img2)
#
# """
#
# 3.由tensor转换为图片
# 经过tensor的处理过程之后，要将tensor形式转换为图片。
# 用到numpy()函数，fromarray()函数。uint8函数
#
# """
#
# # 这里将tensor形式用numpy()函数转为数组形式，
#
# # 并且用transpose将数组转置为PIL能够处理的WxHxC形式。
#
# nimg = img1.numpy().transpose(1, 2, 0)
#
# img = nimg * 255  # 将原来tensor里0-1的数值乘以255，以便转为uint8数据形式，uint8是图片的数值形式。
#
# # 那么此时img就是原料，通过两种方式将img化为图片
#
# # 第一种
#
# # img3 = Image.fromarray(np.uint8(img))  # eg1
#
# # 第二种
#
# img4 = Image.fromarray(img.astype(np.uint8))  # eg2
#
# print(img4)
