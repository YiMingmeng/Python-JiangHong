list1=[9,7,8,3,2,1,55,6]
maxi=list1[0];mini=list1[0];s=0;n=len(list1)
i=n-1
while i>=0:
    if list1[i]>maxi:
        maxi=list1[i]
    if list1[i]<mini:
        mini=list1[i]
    s+=list1[i]
    i-=1
print(n,maxi,mini,s,s/n)
  
