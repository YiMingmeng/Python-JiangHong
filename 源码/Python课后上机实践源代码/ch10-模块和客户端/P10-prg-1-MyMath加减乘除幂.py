#MyMath.py
def add(x, y): #定义函数
    return x + y  #加
def sub(x, y):
    return x - y  #减
def mul(x, y):
    return x * y  #乘
def div(x, y):
    return x / y  #除
def power(x, y):
    return x ** y  #幂
#测试代码
if __name__ == '__main__': #如果独立运行时，则运行测试代码
    print('123 + 100 =', add(123, 100))
    print('123 - 100 =', sub(123, 100))
    print('123 * 100 =', mul(123, 100))
    print('123 / 100 =', div(123, 100))
    print('2 ** 10 =', power(2, 10))

