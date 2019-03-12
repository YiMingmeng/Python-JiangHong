from math import *
class MyMath:
    global PI
    PI  = 3.1415926
    def Perimeter(r):
        return (2 * PI * r)
    def Area(r):
        return (PI * r * r)
    def Surface(r):
        return (4*PI * r * r)
    def Volume(r):
        return( 4 * PI * pow(r, 3) / 3)
r = float(input("请输入半径： "))
print(str.format("圆的周长 = {0:2.2f}", MyMath.Perimeter(r)))
print(str.format("圆的面积 = {0:2.2f}", MyMath.Area(r)))
print(str.format("球的表面积 = {0:2.2f}", MyMath.Surface(r)))
print(str.format("球的体积 = {0:2.2f}", MyMath.Volume(r)))
