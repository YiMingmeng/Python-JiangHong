#求 a 的算术平方根的近似方法
def sqrtA( a ):
    if a<0:
        a = -a
    if a==0:
        return 0
    x1 = 1.0
    while True:
        x2 = (x1 + a / x1 )/2
        if abs(x2-x1)> 1E-6 *( abs(x2)+abs(x1)):
            #如果还没有达到计算精度
            x1 = x2
        else:
            break
    return x2

import math
def sqrtA2( a ):
    x0 = a;x1 = (x0 + a / x0) / 2
    while (abs(x1 - x0) > pow(10, -6)):
        x0 = x1; x1 = (x0 + a / x0) / 2
    return x1
#测试代码
a=2
print( a,"的算术平方根=",sqrtA( a ))
a=3
print( a,"的算术平方根=",sqrtA( a ))


a=2
print( a,"的算术平方根=",sqrtA2( a ))
a=3
print( a,"的算术平方根=",sqrtA2( a ))
