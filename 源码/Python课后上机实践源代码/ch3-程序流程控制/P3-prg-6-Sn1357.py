n=6
s=0
for i in range(1,n+1):
    if i%2==0:
        s-=(2*i-1)
    else:
        s+=(2*i-1)
print(s)
