import math
x = float(input("请输入x："))
i = 1; s = 1; t = 1
while (t >= pow(10,-6)):
    t *= x/i; s += t;  i+=1
print("Pow(e,x) = ",s)
