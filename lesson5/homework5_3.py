"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""

with open("homework3.txt") as file:
    low_salary_list = []
    salaries = []
    i = 0
    for line in file:
        i += 1
        fellow = line.split(", ")
        salaries.append(int(fellow[1]))
        if int(fellow[1]) < 20000:
            low_salary_list.append(fellow[0])
print(f"Сотрудники с зарплатой меньше 20000: {low_salary_list}")
print(f"Средняя величина дохода сотрудников: {sum(salaries) / i}")


