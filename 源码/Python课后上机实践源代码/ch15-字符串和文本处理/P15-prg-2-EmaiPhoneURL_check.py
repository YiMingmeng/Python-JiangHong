import os, re
def check_phone(strPhone): #中华人民共和国电话号码
    regex_phone = re.compile(r'^(\(\d{3}\)|\d{3}-)?\d{8}$')
    result = True if regex_phone.match(strPhone) else False
    return result
def check_ZIP(strZIP):     #中华人民共和国邮政编码
    regex_ZIP = re.compile(r'^\d{6}$')
    result = True if regex_ZIP.match(strZIP) else False
    return result
def check_URL(strURL):     #网站网址
    regex_URL = re.compile(r'^https?://\w+(?:\.[^\.]+)+(?:/.+)*$')
    result = True if regex_URL.match(strURL) else False
    return result
def check_email(strEmail):#email地址
    regex_email = re.compile(r'^[\w\.\-]+@([\w\-]+\.)+[\w\-]+$')
    result = True if regex_email.match(strEmail) else False
    return result
#测试代码
if __name__=='__main__':
    str1 = input("请输入中国电话号码：")
    print(str1,'是有效的电话号码格式吗？', check_phone(str1))
    str2 = input("请输入中国邮政编码：")
    print(str2,'是有效的邮政编码格式吗？', check_ZIP(str2))
    str3 = input("请输入网站网址：")    
    print(str3,'是有效的网站网址格式吗？', check_URL(str3))
