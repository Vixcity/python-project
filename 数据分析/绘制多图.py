# -*- coding: UTF-8 -*-
# @创建时间 : 2020/11/10 16:26
# @开发作者 : Vixcity
# @文件名称 : 绘制多图.py
# @开发工具 : PyCharm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([1,2,3])
y1 = x
y2 = x ** 2
y3 = x ** 3
y4 = x ** 4

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# plt
plt.figure(facecolor='white')
plt.plot(x,y1,label='1次方')
plt.plot(x,y2,label='2次方')
plt.plot(x,y3,label='3次方')
plt.plot(x,y4,label='4次方')
# 图例
plt.legend()

# 面向对象
fig,ax = plt.subplots(
    facecolor='white'
)

ax.plot(x,y1,label='1次方')
ax.plot(x,y2,label='2次方')
ax.plot(x,y3,label='3次方')
ax.plot(x,y4,label='4次方')
ax.legend()

# 多图绘制plt
plt.subplot(221)
plt.plot(x,y1,label='1次方',color='r')
plt.xticks(fontsize=20)
plt.legend()

plt.subplot(222)
plt.plot(x,y2,label='2次方',color='g')
plt.xticks(fontsize=20)
plt.legend()

plt.subplot(223)
plt.plot(x,y3,label='3次方',color='b')
plt.xticks(fontsize=20)
plt.legend()

plt.subplot(224)
plt.plot(x,y4,label='4次方',color='y')
plt.xticks(fontsize=20)
plt.legend()

plt.tight_layout()

# 面向对象
fig,axs = plt.subplots(
    2,
    2,
    facecolor='white',
    figsize=(10,8)
)
axs[0,0].plot(x,y1)
axs[0,1].plot(x,y2)
axs[1,0].plot(x,y3)
axs[1,1].plot(x,y4)

# 四行一列
fig,axs = plt.subplots(
    4,
    1,
    facecolor='white',
    figsize=(4,8),
    sharex='all'
)
axs[0].plot(x,y1)
axs[1].plot(x,y2)
axs[2].plot(x,y3)
axs[3].plot(x,y4)

plt.show()
def main():
    pass


if __name__ == "__main__":
    main()