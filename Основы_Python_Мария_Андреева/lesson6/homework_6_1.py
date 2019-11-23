"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Время перехода между режимами должно составлять 7 и 2 секунды.
Проверить работу примера, создав экземпляр и вызвав описанный метод."""

from time import sleep
from itertools import cycle

class TrafficLight:
    __color = ["Red", "Yellow", "Green", "Yellow"]

    def running(self, main_int, yellow_int):
        col = TrafficLight.__color   # писать везде далее TrafficLight.__color мне показалось громоздким, поэтому придумал типа псевдонима
        for el in cycle(col):
            print(el)
            if el == col[0] or el == col[2]:
                interval = main_int
            if el == col[1] or el == col[3]:
                interval = yellow_int
            sleep(interval)

traffic_light1 = TrafficLight()
traffic_light1.running(7, 2)



