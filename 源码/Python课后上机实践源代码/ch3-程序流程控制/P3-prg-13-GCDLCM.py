import random
m1 = random.randint(0,100)
n1 = random.randint(0,100)
print(str.format("整数1 = {0}, 整数2 = {1}", m1, n1))
if (m1 > n1):
    m = m1; n = n1
else:
    m = n1; n = m1
r=1
while (r != 0):
    r = m % n;m = n;n = r
print(str.format("最大公约数 = {0}, 最小公倍数 = {1:1.0f}", m, m1 * n1 / m))
