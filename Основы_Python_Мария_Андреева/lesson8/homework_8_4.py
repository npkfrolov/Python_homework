"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. """

class Storage:
    pass

class Office_equip:

    def __init__(self, model):
        self.model = model

class Printers(Office_equip):
    nomencl_print = []

    @classmethod  # этот метод выводит словарь моделей без дублей
    def dict_printers(cls):
        return  dict(printers=list(set(cls.nomencl_print)))

    def __init__(self, model):
        super().__init__(model)
        Printers.nomencl_print.append(self.model)

    def __repr__(self):
        return f"{self.model}"      # позволяет распечатать название в словаре

class Scanners(Office_equip):
    nomencl_scan = []

    @classmethod  # этот метод выводит словарь моделей без дублей
    def dict_scanners(cls):
        return dict(scanners=list(set(cls.nomencl_scan)))

    def __init__(self, model):
        super().__init__(model)
        Scanners.nomencl_scan.append(self.model)

    def __repr__(self):
        return f"{self.model}"  # позволяет распечатать название в словаре

class Copiers(Office_equip):
    nomencl_copiers = []

    @classmethod  # этот метод выводит словарь моделей без дублей
    def dict_copiers(cls):
        return dict(copiers=list(set(cls.nomencl_copiers)))

    def __init__(self, model):
        super().__init__(model)
        Copiers.nomencl_copiers.append(self.model)

    def __repr__(self):
        return f"{self.model}"  # позволяет распечатать название в словаре
