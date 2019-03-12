list1=[9,7,8,3,2,1,55,6]
maxi=list1[0];mini=list1[0];s=0
for i in list1:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
    s+=i
print(len(list1),maxi,mini,s,s/len(list1))
  
