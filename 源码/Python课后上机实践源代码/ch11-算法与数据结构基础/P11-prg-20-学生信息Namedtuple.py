#namedtuple.py
from collections import *
import csv,math
StudentRecord = namedtuple('StudentRecord', 'ID, Chinese, Maths, English, IT')
print(' 学号   平均成绩')
for stu in map(StudentRecord._make, csv.reader(open("scores.csv"))):
    print(stu.ID, (int(stu.Chinese)+int(stu.Maths)+int(stu.English)+int(stu.IT))/4)
