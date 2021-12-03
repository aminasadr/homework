from time import sleep

class TrafficLight:
    # атрибуты класса
    __color1 = "red"

    # метод
    def run(self):
        n = 2
        m = 1
        while m < n:
            print("red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("green")
            sleep(7)
            print("yellow")
            sleep(2)
            m += 1
        else:
            print("end")
# объект
color = TrafficLight()
color.run()


class Road:

    def __init__(self, l, w):
        self._l = l
        self._w = w
    def count(self, mass = 25, high = 2):
        mass_asf = self._l * self._w * mass * high
        print(mass_asf)

road = Road(100, 1)
road.count()



class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}
        print("This is worker")

class Position(Worker):
    def get_full_name(self):
        #super().__init__(self.name, self.surname, self.income)
        print(f"full name is {self.name} {self.surname}")
        print(f"income is {sum(self.income.values())}")


work = Worker("Nemo", "Nautilus", "captain", 1000, 10)
position = Position("Nemo", "Nautilus", "captain", 1000, 10)
position.get_full_name()


from random import choice
class Car:
    direction = ["right", "left", "back", "straight"]
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def show_speed(self):
        print(f"speed is {self.speed}")

    def go(self):
        print(f"car {self.name} is going")
    def stop(self):
        print(f"car {self.name} stopped")
    def turn_direction(self):
        print(f"car {self.name} turned {choice(self.direction)}")

class TownCar(Car):
    def show_speed(self):
        #super().__init__(speed)
        if self.speed > 60:
            print(f"{self.speed} is over speed")
        else:
            print(f"town_car is going")
#class SportCar(Car):


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.speed} is over speed")
        else:
            print(f"work_car is going")

class PoliceCar(Car):
    def call(self):
        print("police")



car = Car(60, "red", "niva", "false")
car.show_speed()
car.go()
car.stop()
car.turn_direction()
town_car = TownCar(90, "red", "niva", "true")
town_car.show_speed()
work_car = WorkCar(30, "red", "niva", "true")
work_car.show_speed()
police = PoliceCar(30, "red", "niva", "true")
police.call()


class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки {self.title}")
class Pen(Stationary):
    def draw(self):
        print(f"Запуск отрисовки {self.title} by pen")
class Pencil(Stationary):
    def draw(self):
        print(f"Запуск отрисовки {self.title} by pencil")
class Handle(Stationary):
    def draw(self):
        print(f"Запуск отрисовки {self.title} by handle")


stat = Stationary("f")
pen = Pen("Flower")
pencil = Pencil("red")
handle = Handle("go away")

all = [stat, pen, pencil, handle]
for i in all:
    i.draw()




