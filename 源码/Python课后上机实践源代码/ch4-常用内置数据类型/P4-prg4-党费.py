salary = int(input("请输入有固定工资收入的党员的月工资："))  #月工资
if (salary > 0 and salary <= 400): f = 0.5 / 100 * salary
elif (salary > 400 and salary <= 600): f = 1.0 / 100 * salary
elif (salary > 600 and salary <= 800): f = 1.5 / 100 * salary
elif (salary > 800 and salary <= 1500): f = 2.0 / 100 * salary
elif (salary > 1500): f = 3.0 / 100 * salary
else: print("月工资输入有误！")
print(str.format("月工资 = {0}，交纳党费 = {1}", salary, f))
