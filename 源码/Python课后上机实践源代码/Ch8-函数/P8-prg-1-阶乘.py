def fact(n): #声明函数，返回值
    if n==0:
        f=1
    else:
        f=n*fact(n-1)
    return(f)
n=int(input("请输入整数n（n>=0）："))
print(n,"!=",fact(n))      #调用函数
