import random,math
a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
print(str.format("原始值：  a={0}， b={1}， c={2}", a, b, c))
a1 = a;b1 = b;c1 = c  # 保留a,b,c的值，以方便两种方法的比较
#方法一：先a和b比较，使得a<b；然后a和c比较，使得a<c，此时a最小；最后b和c比较，使得b<c
if (a > b):
    t = a;a = b;b = t
if (a > c):
    t = a;a = c;c = t
if (b > c):
    t = b;b = c;c = t
print(str.format("(方法一)升序值：  a={0}， b={1}， c={2}", a, b, c))
a = a1;b = b1;c = c1  # 恢复a,b,c的值，使用第二种方法
#方法二：利用Max函数和Min函数求a、b、c三个数中最大数、最小数，而三个数之和减去最大数和最小数就是中间数
Nmax = max(a, b, c)
Nmin = min(a, b, c)
Nmid = a + b + c - Nmax - Nmin
a = Nmin;b = Nmid;c = Nmax
print(str.format("(方法二)升序值：  a={0}， b={1}， c={2}", a, b, c))
