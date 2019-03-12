#圆面积、球体积
import math
PI = 3.14    #定义变量
def area(r): #定义函数
    return PI*r*r  #圆面积
def volume(r):
    return 4*PI*pow(r,3)/3  #球体体积
def main():
    r = float(input("请输入半径："))#输入半径并转换为浮点数
    print('圆面积={0:2.2f}'.format(area(r)))
    print('球体体积={0:2.2f}'.format(volume(r)))
if __name__ == '__main__': #如果独立运行时，则运行测试代码
    main()

