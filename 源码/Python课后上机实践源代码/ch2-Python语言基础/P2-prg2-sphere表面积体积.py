import math
r = float(input("请输入球的半径：")) #输入球的半径并转换为浮点数
area = 4 * math.pi * r ** 2
volume = 4*math.pi*r ** 3/3
print(str.format("球为表面积为：{0:2.2f}，体积为：{1:2.2f}", area, volume))
