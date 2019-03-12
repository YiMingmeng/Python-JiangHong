def min_n(a, b, *c):
    min_value = a
    if min_value > b:
        min_value = b
    for n in c:
        if min_value > n:
            min_value = n
    return min_value
#测试代码
print("最小值为",min_n(8, 2))
print("最小值为",min_n(16, 1, 7, 4, 15))
