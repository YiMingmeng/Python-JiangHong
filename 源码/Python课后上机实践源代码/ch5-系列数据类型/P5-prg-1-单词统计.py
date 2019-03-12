Number = 0   #统计单词个数
word = False #判断是否是单词
strs=input("请输入字符串：")
for i in range(len(strs)):
    ch=strs[i]
    if (ch == ' '): word = False
    elif (not word):
        word = True; Number+=1
#print("字符串为：", strs);
print("其中的单词总数有：", Number)
