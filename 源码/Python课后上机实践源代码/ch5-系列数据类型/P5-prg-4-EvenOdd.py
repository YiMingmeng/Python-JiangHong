s=[9,7,8,3,2,1,5,6]
print( "变换前,s=", s) #原列表内容
for i in range( 0,  len(s)):
    if (s[i] % 2) ==0:   #如果第i个元素是偶数
        s[i] = s[i] * s[i]
print( "变换后,s=",s)
  
