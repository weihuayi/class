import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)

# 创建画布
fig = plt.figure()

# 创建坐标系
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 第一个坐标系的范围
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # 第二个坐标系的范围

axes1.plot(x, y, 'r')
axes2.plot(x, y, 'g')
fig.savefig('myfirstfig.eps')
#plt.show()
