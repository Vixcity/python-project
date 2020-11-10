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
plt.figure(facecolor="white",figsize=(6,6),dpi=100)

# 标题
plt.title('我是标题',fontsize=30,color='r')

# 数据显示
plt.plot(df['A'],df['B'])

# X轴标题
plt.xlabel('我是X轴',
           fontsize=24,
           color='g')

# Y轴标题
plt.ylabel('我是Y轴',
           fontsize=24,
           color='b',
           rotation=0,
           labelpad=50)

# 刻度
plt.xlim([-1,5])
plt.ylim([0,20])

# 自定义有多少个刻度
# plt.xticks([1,2,3,4],fontsize=20)
# plt.yticks([0,5,10,15,20],fontsize=20)

# 自定义刻度的格子大小
# 大刻度
plt.gca().xaxis.set_major_locator(
    plt.MultipleLocator(2)
)
# 小刻度
plt.gca().xaxis.set_minor_locator(
    plt.MultipleLocator(0.5)
)

# Y轴
plt.gca().yaxis.set_major_locator(
    plt.MultipleLocator(5)
)
plt.gca().yaxis.set_minor_locator(
    plt.MultipleLocator(1)
)

# 网格
plt.grid(color='y')

# 显示图片
plt.show()

def main():
    pass


if __name__ == "__main__":
    main()