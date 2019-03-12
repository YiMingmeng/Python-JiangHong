import random
A=set()
for i in range(10):
    A.add(random.randint(0,10))  #随机产生一个0~10的整数，添加到A
B=set()
for i in range(10):
    B.add(random.randint(0,10))  #随机产生一个0~10的整数，添加到B
print("集合的内容、长度、最大值、最小值分别为：")
print(A,len(A),max(A),min(A))
print(B,len(B),max(B),min(B))
print("A和B的并集、交集和差集分别为：")
print(A|B,A&B,A-B)
