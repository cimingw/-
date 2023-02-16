# 导入需要使用的包
import numpy as np
import math
import matplotlib.pyplot as plt
e = math.e

# 定义一个sigmoid函数
def sigmoid(x):
    return 1 / (1 + pow(e, -x))

# 定义一个softplus函数
def softplus(x):
    return math.log(1 + pow(e, x))

# 定义一个tanh函数
def tanh(x):
    return (e ** x - e ** (-x)) / (e ** x + e ** (-x))

# 定义一个leakyrelu函数
def leakyrelu(x):
    return max(x, 0.1 * x)

# 定义一个mish函数
def mish(x):
    return x * tanh(softplus(x))

# 限定x,y坐标轴范围为(-5,5),并在其中产生1000个相应的点
x = np.linspace(-5, 5, 1000)
y0 = np.linspace(-5, 5, 1000)
y1 = np.linspace(-5, 5, 1000)
y2 = np.linspace(-5, 5, 1000)
# 将函数值赋值给上述产生的点
for i in range(1000):
    y0[i] = sigmoid(x[i])
    y1[i] = leakyrelu(x[i])
    y2[i] = mish(x[i])
# 绘制函数图像
plt.plot(x, y0, color='blue', linewidth=1, label='sigmoid')
plt.plot(x, y1, color='red', linewidth=1, label='leakyrelu')
plt.plot(x, y2, color='orange', linewidth=1, label='mish')
plt.title('sigmoid, leakyrelu and Mish functions', fontdict={'family': 'Times New Roman', 'size': 14})
plt.xticks(fontproperties = 'Times New Roman', size = 14)
plt.legend(prop={'family' : 'SimSun', 'size' : 14})
plt.yticks(fontproperties = 'Times New Roman', size = 14)
plt.grid()
plt.savefig('mish.jpg', dpi=600, bbox_inches='tight')
plt.show()