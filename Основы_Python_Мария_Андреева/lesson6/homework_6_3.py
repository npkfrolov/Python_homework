"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"profit": profit, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_full_profit).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""

class Worker:
    name = []
    surname = []
    position = []
    salary = 0
    bonus = 0
    _income = {"salary": salary, "bonus": bonus}
    i = 0

    def __init__(self):
        Worker.name = input("Имя ")
        Worker.surname = input("Фамилия ")
        Worker.position = input("Должность ")
        Worker.salary = input("Зряплата ")
        Worker.bonus = input("Премия ")
        Worker._income.update({"salary": Worker.salary, "bonus": Worker.bonus})
        Worker.i += 1


class Position(Worker):

    def get_full_name(self):
        print(f"{Worker.name} {Worker.surname}")

    def get_full_profit(self):
        print(int(Worker._income.setdefault("salary")) + int(Worker._income.setdefault("bonus")))

fellow = Position()
fellow.get_full_name()
fellow.get_full_profit()
fellow2 = Position()
fellow2.get_full_name()
fellow2.get_full_profit()
fellow3 = Position()
fellow3.get_full_name()
fellow3.get_full_profit()
