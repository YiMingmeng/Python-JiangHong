from  math import *
x=float(input("请输入x：   "))
#  方法一：利用“一句单分支语句”实现
y = (x * x - 3 * x) / (x + 1) + 2 * pi + sin(x)
if (x < 0):  y = log(-5 * x) + 6 * sqrt(abs(x) + pow(e, 4)) - pow(x + 1, 3)
print(str.format("方法一：x = {0}，y = {1}", x, y))
#  方法二：利用“两句单分支语句”实现
if (x >= 0):   y = (x * x - 3 * x) / (x + 1) + 2 * pi + sin(x)
if (x < 0):    y = log(-5 * x) + 6 * sqrt(abs(x) + pow(e, 4)) - pow(x + 1, 3)
print(str.format("方法二：x = {0}，y = {1}", x, y))
#  方法三：利用“双分支结构”实现
if (x >= 0):  y = (x * x - 3 * x) / (x + 1) + 2 * pi + sin(x)
else:    y = log(-5 * x) + 6 * sqrt(abs(x) + pow(e, 4)) - pow(x + 1, 3)
print(str.format("方法三：x = {0}，y = {1}", x, y))
#  方法四：利用“条件运算符”4种方法实现
y =  (x * x - 3 * x) / (x + 1) + 2 * pi + sin(x) if (x >= 0) else log(-5 * x) + 6 * sqrt(abs(x) + pow(e, 4)) - pow(x + 1, 3)
print(str.format("方法四：x = {0}，y = {1}", x, y))
