import calendar
import locale
textcal = calendar.TextCalendar() #创建文本日历
textcal.pryear(2017)              #打印2017年一年的日历 
loc = locale.getlocale()                               #获取当前系统的locale（本地化配置）
localtextcal = calendar.LocaleTextCalendar(locale=loc) #返回指定locale的月份和星期信息
localtextcal.prmonth(2017, 12,w=8)                     #打印2017年12月的日历，宽度为8，居中
