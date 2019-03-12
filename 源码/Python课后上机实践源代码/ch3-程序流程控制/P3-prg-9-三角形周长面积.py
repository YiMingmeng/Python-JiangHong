import math
a=float(input("请输入三角形的边A：   "))
b=float(input("请输入三角形的边B：   "))
c=float(input("请输入三角形的边C：   "))
if (a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a):
    print(str.format("三角形三边分别为： a={0}, b={1}, c={2}", a, b, c))
    p = a + b + c
    h = p / 2
    area = math.sqrt(h * (h - a) * (h - b) * (h - c))
    print(str.format("三角形的周长 = {0:2.1f}，面积 = {1:2.1f}", p, area))
else: print("无法构成三角形！")
