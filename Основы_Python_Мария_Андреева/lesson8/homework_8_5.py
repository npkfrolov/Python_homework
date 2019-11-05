"""Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь."""

from homework_8_4 import Storage, Printers, Office_equip, Scanners, Copiers


class Partners:  # контрагенты (поставщики и получатели)
    pass


class Provider(Partners):  # поставщики

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Office(Partners):  # получатели
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class St_Activities:  # движение по складу
    deliv_list = []
    ship_list = []

    @staticmethod
    def show_stocks():
        if isinstance(St_Activities.deliv_list[0], Printers):  # не работает isinstance, поэтому список из чисел не формируетсяif isinstance(St_Activities.deliv_list[0], Printers)]  # не работает isinstance, поэтому список из чисел не формируется
            return f"Остатки принтеров на складе - {deliv_stat}"

    def __init__(self, invoice, date, partner, items, amount):
        self.invoice = invoice
        self.date = date
        self.partn = partner
        self.items = items
        self.amount = amount


class Delivery(St_Activities):  # регистрация поставок на склад
    _i_del = 0
    journal_deliv = []

    def __init__(self, invoice, date, partner, items, amount):
        super().__init__(invoice, date, partner, items, amount)
        self.date = date
        self.invoice = invoice
        self.partner = partner
        self.items = items
        self.amount = amount
        Delivery._i_del += 1
        reg_del = (Delivery._i_del, self.date, self.invoice, self.partner, self.items, self.amount)
        Delivery.journal_deliv.append(reg_del)
        stat_del = [self.items, self.amount]
        Delivery.deliv_list.append(stat_del)


class Shipment(St_Activities):  # регистрация отгрузок со склада
    _i_ship = 0
    journal_ship = []

    def __init__(self, invoice, date, partner, items, amount):
        self.date = date
        self.invoice = invoice
        self.partner = partner
        self.items = items
        self.amount = amount
        Shipment._i_ship += 1
        reg_ship = (Shipment._i_ship, self.date, self.invoice, self.partner, self.items, self.amount)
        Shipment.journal_ship.append(reg_ship)
        stat_ship = [self.items, self.amount]
        Shipment.ship_list.append(stat_ship)


# Не было времени обернуть ввод данных в цикле while через input, пошел простым путем
printer1 = Printers("HP")
printer2 = Printers("Epson")
scanner1 = Scanners("Canon")
copier1 = Copiers("Xerox")
provider1 = Provider("Промокашка")
provider2 = Provider("Спецоборонэкспорт")
office1 = Office("Рога и копыта")
office2 = Office("Воши Кыш")
deliv1 = Delivery(8, "2005-01-01", provider1, scanner1, 5)
deliv2 = Delivery(11, "2001-01-01", provider2, printer1, 2)
deliv3 = Delivery(15, "2006-01-01", provider2, printer2, 3)
deliv4 = Delivery(55, "2006-05-01", provider1, copier1, 6)
ship1 = Shipment(1, "2005-01-01", office1, scanner1, 1)
ship2 = Shipment(2, "2001-01-01", office2, printer2, 1)
ship3 = Shipment(3, "2006-01-01", office1, printer1, 1)
ship4 = Shipment(4, "2007-01-01", office1, copier1, 1)
print(Delivery.journal_deliv)  # выводит журнал поставок на склад
print(Shipment.journal_ship)  # выводит журнал отгрузок со склада
print(Printers.dict_printers())  # вывод словаря моделей принтеров
print(Scanners.dict_scanners())  # вывод словаря моделей сканеров
print(Copiers.dict_copiers())  # вывод словаря моделей ксероксов
print(Delivery.deliv_list)
print(Shipment.ship_list)
print(St_Activities.show_stocks())
