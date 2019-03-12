class Temperature:
    def __init__(self, d):
        self.degree = d
    def ToFahrenheit(self):
        return (self.degree * 9 / 5) + 32
    def ToCelsius(self):
        return (self.degree - 32) * 5 / 9
d1 = float(input("请输入摄氏温度： "))
celsius = Temperature(d1)
print(str.format("摄氏温度 = {0}，华氏温度 = {1} ", d1, celsius.ToFahrenheit()))
d2 = float(input("请输入华氏温度： "))
celsius = Temperature(d2)
print(str.format("华氏温度 = {0}，摄氏温度 = {1} ", d2, celsius.ToCelsius()))
