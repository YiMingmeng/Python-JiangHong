fac = 1
n = -1
while (n < 0):
    n=int(input("请输入非负整数n："))
# 方法一：for循环
for i in range(1, n+1): fac *= i
print(str.format("  for循环：{0}! = {1}", n, fac))
# 方法二：while循环
i = 1; fac = 1
while (i <= n):
    fac *= i; i+=1
print(str.format("while循环：{0}! = {1}", n, fac))
