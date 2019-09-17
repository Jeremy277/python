#定义车类
#定义电动车

class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def run(self):
        print('run')


class Electric_car(Car):

    def __init__(self,brand,speed,battery):
        self.battery = battery
        #self指的是对象 谁调用就指的是谁,此处指的是电动车
        super().__init__(brand,speed)


c01 = Car('奔驰','230km/h')
c02 = Electric_car('特斯拉','120km/h',2500)

c01.run()
c02.run()

print(c02.brand,c02.speed,c02.battery)