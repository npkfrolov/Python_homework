"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

#from abc import ABC, abstractmethod

outgo = []

def total():
    return sum(outgo)

class Dress():
    def name(self, name):
        self.name = name

class Coat(Dress):
    def __init__(self, v):
        self.v = v
        self.result = self.v / 6.5 + 0.5
        outgo.append(self.result)

    def __str__(self):
        return f"{self.result}"

class Suit(Dress):
    def __init__(self, h):
        self.h = h
        self.result = 2 * self.h + 0.3
        outgo.append(self.result)

    def __str__(self):
        return f"{self.result}"

suit1 = Suit(3)
coat1 = Coat(6.5)
suit2 = Suit(5)
coat2 = Coat(2)
print(suit1)
print(suit2)
print(coat1)
print(coat2)
print(f"общий расход материала: {total()}")
