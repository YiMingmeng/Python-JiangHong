h=100.0;s = 100
for i in range(2,11):
    h = h / 2; s += h
print(str.format("小球在第10次落地时，共经过{0:2.2f}米",s))
print(str.format("第10次反弹{0:2.2f}米",h))
