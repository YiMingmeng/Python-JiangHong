#求序列类型的最大值和最小值
def getMaxMin(s):
    maxi  = s[0]
    mini  = s[0]
    for i in range( 0, len(s)):
        if maxi<s[i]:
            maxi = s[i]
        if mini>s[i]:
            mini = s[i]
    return maxi,mini,len(s)
#测试代码
list1=[9,7,8,3,2,1,55,6]
x1,y1,z1 = getMaxMin(list1)
print("list=", list1)
print("最大值=",x1, ",最小值=", y1, ",元素个数=", z1)

list2=["apple","pear","melon","kiwi"]
x2,y2,z2 = getMaxMin(list2)
print("list=", list2)
print("最大值=",x2, ",最小值=", y2, ",元素个数=", z2)

list3="TheQuickBrownFox"
x3,y3,z3 = getMaxMin(list3)
print("list=", list3)
print("最大值=",x3, ",最小值=", y3, ",元素个数=", z3)

list4=(9,7,8,3,2,1,55,6)
x4,y4,z4 = getMaxMin(list4)
print("list=", list4)
print("最大值=",x4, ",最小值=", y4, ",元素个数=", z4)
