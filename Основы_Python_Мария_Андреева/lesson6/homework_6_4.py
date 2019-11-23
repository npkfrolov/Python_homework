"""Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также несколько методов:
go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)."""

class Transport():
    speed = 0
    color = []
    name = []
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

class TownCar(Transport):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class SportCar(Transport):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Transport):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Transport):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

