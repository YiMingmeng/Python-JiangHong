def fab(n):
    if n <= 2: return(1)
    else:
        return(fab(n-1)+fab(n-2))
n=20
for i in range(1,n+1):
    print(format(fab(i),">5"),end=' ')
    if(i % 10==0):print("\n")
