import matplotlib.pyplot as plt

plt.figure()
plt.show()


fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
plt.show()

import numpy as np
x = np.linspace(0, 10, 10)
y = np.sin(x)
 
# 创建画布
fig = plt.figure()
# 创建坐标轴
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 第一个坐标轴的范围
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # 第二个坐标轴的范围
 
ax1.plot(x, y, 'r')
ax2.plot(x, y, 'g')
plt.show()

fig = plt.figure(figsize=(16,8), dpi=100) # dpi

先创建画布，再创建坐标系，最后在坐标系上绘图。