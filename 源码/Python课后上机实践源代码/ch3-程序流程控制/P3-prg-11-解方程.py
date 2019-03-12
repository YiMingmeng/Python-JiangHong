import math
a=float(input("请输入系数a：   "))
b=float(input("请输入系数b：   "))
c=float(input("请输入系数c：   "))
if (a == 0):
    if (b == 0):print("此方程无解！")
    else:print(str.format("此方程的解为： {0}", -c / b))
else:
    delta = b * b - 4 * a * c
    if (delta > 0):
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(str.format("此方程有两个不等实根： {0} 和 {1} ", x1, x2))
    else:
        if (delta == 0): print(str.format("此方程有两个相等实根： {0}", -b / (2 * a)))
        else:
            realPart = -b / (2 * a)
            imagPart = math.sqrt(-delta) / (2 * a)
            print(str.format("此方程有两个不等实根： {0}+{1}i 和 {0}-{1}i  ", realPart, imagPart))
