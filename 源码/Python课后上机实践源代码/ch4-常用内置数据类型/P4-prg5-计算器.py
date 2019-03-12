right=True
x = float(input("请输入操作数x："))
y = float(input("请输入操作数y："))
op = str(input("请输入操作符：")) 
if(op=='+'):r = x + y
elif (op=='-'):r = x - y
elif (op=='*'):r = x * y
elif (op=='/'):
    if(y==0):
        print("分母=0，零除异常！")
        right=False
    else: r = x / y
elif (op=='%'):
    if(y==0):
        print("分母=0，零除异常！")
        right=False
    else: r = x % y
if right: print(x,op,y,'=',r)
