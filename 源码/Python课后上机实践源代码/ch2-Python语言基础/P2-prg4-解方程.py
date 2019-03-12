#chapter02\module1.py
#求解方程x* x -10*x + 16 = 0 
import math
a = 1; b = -10; c = 16
x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
print('方程x* x -10*x + 16 = 0 的解为：', x1, x2)

