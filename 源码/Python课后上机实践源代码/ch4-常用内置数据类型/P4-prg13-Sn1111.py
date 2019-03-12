import random
n = random.randint(1,10)    #随机产生一个1~10以内的整数
t=0;s=0
for i in range(1,n+1):
    t=t*10+1
    s+=t
print("n=",n,"sn=",s)

