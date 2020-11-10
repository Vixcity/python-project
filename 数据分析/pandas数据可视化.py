# -*- coding: UTF-8 -*-
# @创建时间 : 2020/11/10 14:05
# @开发作者 : Vixcity
# @文件名称 : pandas数据可视化.py
# @开发工具 : PyCharm
import matplotlib.pyplot as plt
# plt.style.use('seaborn-white')  设置风格
# plt.style.available 查看可用风格

# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# 中文显示问题设置

# 显示图片↑
import  pandas as  pd
import seaborn as sns
import numpy as np
sns.set_style('white')
s = pd.Series(
    [1,2,3],
    index = list('ABC')
)
# 这三种方法所展示的效果一样
# 直线图
# s.plot()
# s.plot(kind='line')
# s.plot.line

# 默认 是line类型
# s.plot(x="X",y='Y')

# bar 条形图  柱状图
# s.plot.bar(x='X',y='Y')

# bar 水平条形图  横向柱状图
# s.plot.barh(x='X',y='Y')

# pie 饼图
# s.plot.pie()

# scatter 散点图
# df = pd.DataFrame(np.random.randn(1000,2),columns=['X','Y'])
# df.plot.scatter(x="X",y="Y")

# hexbin 六角箱图
# df = pd.DataFrame(np.random.randn(1000,2),columns=['X','Y'])
# df.plot.hexbin(x="X",y="Y",gridsize=8)

# hist 直方图
# x=[0,1,2,3,4,5]
# y=[1,2,2,2,3,3]
# s.plot.hist()

# kde/density 密度图
# s=pd.Series(np.random.randn(1000))
# s.plot.kde()
# s.plot.density()

# box 箱型图
# pf=pd.DataFrame(np.random.rand(10,2),columns=['A','B'])
# pf.plot.box()

# area 面积图
# df=pd.DataFrame(np.random.rand(10,2),columns=['A','B'])
# df.plot.area()

# 显示图片
plt.show()
# 保存图片
# plt.savefig('x.png')
def main():
    pass


if __name__ == "__main__":
    main()