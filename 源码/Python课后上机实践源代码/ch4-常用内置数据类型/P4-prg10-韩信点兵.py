print("0~1000中用3除余2，用5除余3，用7除余2的数有：")
for n in range(1001):
    if (n % 3 == 2 and n % 5 == 3 and n % 7 == 2): print(n,end=' ')
                
