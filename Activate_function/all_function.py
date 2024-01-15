# -*- coding: UTF-8 -*-
''' 
@File    ：ReLU.py
@IDE     ：PyCharm 
@Author  ：Wangzyhao
@Date    ：2024/1/15 14:37 
'''

import torch
from torch import nn
import matplotlib
import matplotlib.pyplot as plt

"""

一、ReLU函数

    ReLU(x) = max(0,x)

可视化：
func = nn.ReLU()
x = torch.arange(start=-2, end=2, step=0.01)
y = func(x)
plt.plot(x.numpy(), y.numpy())
plt.title("relu")
#plt.savefig("relu.jpg")
plt.show()



二、Sigmoid函数

    Sigmoid = 1/(1+exp(-x))

可视化：
func = nn.Sigmoid()
x = torch.arange(-10, 10, 0.01)
y = func(x)
plt.plot(x.numpy(), y.numpy())
plt.title("Sigmoid")
plt.savefig("Sigmoid.jpg")
plt.show()


三、Tanh函数

sinh(x) = (exp(x)-exp(-x))/2
cosh(x) = (exp(x)+exp(-x))/2

    Tanh(x) = sinh(x) * cosh(x)

func = nn.Tanh()
x = torch.arange(-10, 10, 0.01)
y = func(x)
plt.plot(x.numpy(), y.numpy())
plt.title("Tanh")
plt.savefig("Tanh.jpg")
plt.show()


四、Silu函数

    Silu(x) = x * Sigmoid(x)

func = nn.SiLU()
x = torch.arange(start=-10, end=10, step=0.01)
y = func(x)
plt.plot(x.numpy(), y.numpy())
plt.title("SiLU")
plt.savefig("SiLU.jpg")
plt.show()


五、Mish函数

    mish(x) = x * tanh(softplus(x)) = x * tanh(ln(1+exp(x))) 


softplus(x) = ln(1+exp(x))
"""


def mish(x):

    return x * torch.tanh(torch.nn.functional.softplus(x))

x = torch.arange(-10, 10, 0.01)
y = mish(x)
plt.plot(x.numpy(), y.numpy())
plt.title("mish")
plt.savefig("mish.jpg")
plt.show()





