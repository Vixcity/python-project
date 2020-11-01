# 0b是表示二进制的数，默认也是10进制打印输出的,表示二进制的话是0b打头
b = 0b101101101
print(b)
# 0o是表示八进制的数，0o打头
c = 0o555
print(c)
# 0x是表示八进制的数，0x打头
d = 0x16d
print(d)
# python 2 和 python 3 的区别
# 八进制的表示方式python里面0o开始的数字表示8进制，python2里面0开头的也可以表示八进制，但是python3就不行了

# 内置函数进制转换
print(bin(365)) # 二进制
print(oct(365)) # 八进制
print(hex(365)) # 十六进制

# 数据类型转换
# 例如:
e = input('请输入您的密码:')
_e = int(e)
print(_e + 1)

# int 类型转换
abc = '1a2c'
_abc = int(abc,16) # 后面的参数是进制数
print(_abc)

# 超出f部分的英文字母的不能转换，其他进制数原理相同

{}  # 这个是空字典
s = set()  #这个鬼东西是空集合，用了set方法
print(bool(s))