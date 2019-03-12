sumAll=0;sum_odd = 0; sum_even = 0
for i in range(1, 101):
    sumAll+=i
    if i % 2 != 0:      #奇数
        sum_odd += i
    else:               #偶数
        sum_even += i
print("1~100中所有数的和为:", sumAll)
print("1~100中所有奇数的和:", sum_odd)
print("1~100中所有偶数的和:", sum_even)
