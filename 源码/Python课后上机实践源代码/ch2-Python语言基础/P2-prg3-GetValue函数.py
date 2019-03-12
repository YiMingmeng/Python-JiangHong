#GetValue.py
def getValue(b,r,n): #定义函数getValue
    v = b*((1+r)**n) 
    return v
nb = float(input("请输入本金：")) #输入本金并转换为浮点数
nr = float(input("请输入年利率：")) #输入年利率并转换为浮点数
ny = int(input("请输入年份：")) #输入年份并转换为整数
print(str.format("最终收益为：{0:2.2f}",getValue(nb,nr,ny))) #调用函数getValue,打印结果
