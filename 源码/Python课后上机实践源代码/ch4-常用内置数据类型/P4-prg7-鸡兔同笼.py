h = int(input("请输入总头数： "))       #total heads of chicken & rabbit
f = 1
while (f % 2 != 0):
    f = int(input("请输入总脚数(必须是偶数)："))        #total feet of chicken & rabbit
# 方法一：利用循环
solution = False     # 判断是否有解
for c in range(0,h+1):
    r = h - c
    if (2 * c + 4 * r == f):
        print(str.format("方法一：鸡：{0:1.0f} 只， 兔：{1:1.0f} 只", c, r))
        solution = True
if (not solution): print("方法一：无解，请重新运行测试！")
#方法二：解方程
r = f / 2 - h
c = h - r
solution = False     # 判断是否有解
if (r >= 0 and  c >= 0):
    print(str.format("方法二：鸡：{0:1.0f} 只， 兔：{1:1.0f} 只", c, r))
    solution = True
if (not solution): print("方法二：无解，请重新运行测试！")
