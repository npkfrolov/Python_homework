# coding=utf-8
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
# As two alternative solutions are applied, the result is printed twice

invitation = "Enter number of month (1-12): "
my_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # for the 1st solution
my_dict = {'winter': [1, 2, 12], 'spring':[3, 4, 5], 'summer':[6, 7, 8], 'autumn':[9, 10, 11]} # for the 2nd solution

while True: # 1st solution
    num_month = int(raw_input(invitation))
    if num_month > 12:
        continue
    elif num_month < 1:
        continue
    else: break


for el in my_list:
    if num_month == el:
        ind_list = my_list.index(num_month)
        if ind_list < 3:
            season = "winter"
            break
        if ind_list < 6:
            season =  "spring"
            break
        if ind_list < 9:
            season = "summer"
            break
        if ind_list <12:
            season = "autumn"

print ("Month number %s belongs to %s (1st solution)" % (num_month, season))

for key, value in my_dict.items():  # 2nd solution
    if value == num_month:
        season = my_dict.keys()
        break

print ("Month number %s belongs to %s (2nd solution)" % (num_month, season))
