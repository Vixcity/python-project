# i = 0
# while i < 9:
#     i+=1
#     j=0
#     while j<i:
#         j+=1
#         # print(str(j)+'*'+str(i)+'='+str(j*i),end='    ')
#         print(j,'*',i,'=',(j*i),sep="",end='\t')
#         #sep 是把空格转换成替代字
#     print()

# num = 0
# num1 = 0
# while num < 100:
#     num+=1
#     num1 = num+num1
#
# print(num1)
#
# num2 = 0
# for i in range(0,101):
#     num2+=i
# print(num2)

# count = 0
# for i in range(0,100):
#     if i%10==2 and i%3==0:
#         count+=1
# print(count)

count = 0
num = int(input('请输入一个正整数'));
while True:
    count += 1
    num //= 10
    if num == 0:
        break
print('您输入的是',count,'位数',sep='')

x='asdasdasdasdas'
x.find(a)