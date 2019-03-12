from math import *
a=float(input("请输入直角三角形的直角边A(>0)：   "))#直角边A
b=float(input("请输入直角三角形的直角边B(>0)：   "))#直角边B 
c = sqrt(pow(a, 2) + pow(b, 2))#斜边C
print(str.format("直角三角形三边分别为： a={0:1.1f}, b={1:1.1f}, c={2:1.1f}", a, b, c))
p = a + b + c   #周长
h = p / 2
area = sqrt(h * (h - a) * (h - b) * (h - c)) #面积
print(str.format("三角形的周长 = {0:1.1f}，面积 = {1:1.1f}", p, area)) #显示周长和面积
sinA = a / c
aAngle = round(asin(sinA) * 180 / pi, 0)#锐角A
cosB = a / c
bAngle = round(acos(sinA) * 180 / pi, 0)#锐角B
print(str.format("三角形两个锐角的度数分别为： {0:1.1f} 和 {1:1.1f}", aAngle, bAngle))
