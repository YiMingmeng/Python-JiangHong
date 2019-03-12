from calendar import *
def ndays(y,m):
    #每个月的正常天数
    monthDay=[31,28,31,30,31,30,31,31,30,31,30,31]
    days = monthDay[ m-1]
    if (m==2 and isleap(y)):
        days+=1
    return(days)
def fromdays(y,m,d):
    days = 0
    for i in range(1,y):
        days += 365
        if(isleap(i)): days+=1
    for i in range(1,m):
        days += ndays(y,i)
    days+=d
    return(days)
#测试代码
y=int(input("请输入年份（>=1），否则为1："))
m=int(input("请输入月份（1~12），否则<1为1、>12为12："))
d=int(input("请输入日期（1~31），否则<1为1、>ndays(y,m)为ndays(y,m)："))
if y<1: y=1
if m<1: m=1
if m>12: m=12
if d<1: d=1
if d>ndays(y,m): d=ndays(y,m)
print("从1年1月1日到",y,"年",m,"月",d,"日共",fromdays(y,m,d),"天")




