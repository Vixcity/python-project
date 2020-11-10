# -*- coding: UTF-8 -*-
# @创建时间 : 2020/11/10 15:26
# @开发作者 : Vixcity
# @文件名称 : pyplot-style.py
# @开发工具 : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'A':[1,2,2,4]
})
df['B'] = df['A'] ** 2

# 中文显示必备
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 显示的一些参数
fig,ax=plt.subplots(
    facecolor="white",
    figsize=(6,6),
    dpi=100
)
ax.plot(df['A'],df['B'])
# 标题
ax.set_title('我是标题',fontsize=30,color='r')

# X轴标题
ax.set_xlabel('我是X轴',
           fontsize=24,
           color='g')

# Y轴标题
ax.set_ylabel('我是Y轴',
           fontsize=24,
           color='b',
           rotation=0,
           labelpad=50)

# 刻度
ax.set_xlim([-1,5])
ax.set_ylim([0,20])

# 自定义有多少个刻度
# ax.set_xticks([1,2,3,4])
# ax.set_yticks([1,4,9,16])
# ax.tick_params(labelsize=20)

# 自定义刻度的格子大小
# 大刻度
ax.xaxis.set_major_locator(
    plt.MultipleLocator(2)
)
# 小刻度
ax.xaxis.set_minor_locator(
    plt.MultipleLocator(0.5)
)

# Y轴
ax.yaxis.set_major_locator(
    plt.MultipleLocator(5)
)
ax.yaxis.set_minor_locator(
    plt.MultipleLocator(1)
)

# 网格
ax.grid(color='y')

# 显示图片
plt.show()

def main():
    pass


if __name__ == "__main__":
    main()