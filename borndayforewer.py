"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


# Вариант 1
#
# def year_day_birth():
#     year = input('Ввведите год рождения А.С.Пушкина:')
#     while year != '1799':
#         print("Не верно")
#         year = input('Ввведите год рождения А.С.Пушкина:')
#
#     day = input('Ввведите день рождения Пушкин?')
#     while day != '6':
#         print("Не верно")
#         day = input('В какой день июня родился Пушкин?')
#     print('Верно')

# year_day_birth()

# Вариант 2

def born_date(question, date):
    ask = input(question)
    while ask != date:
        print("Неверно!")
        ask = input(question)


born_date("Введите год рождения А.С. Пушкина: ", '1799')
born_date("Введите день рождения А.С. Пушкина в формате 'dd.mm': ", '06.06')
print("Верно")


#Вариант 3

# pushkin_year_of_birth = "1799"
# pushkin_day_of_birth = "06.06"
# def day():
#     day_of_birth = input("Введите день рождения А.С. Пушкина: ")
#     while day_of_birth != pushkin_day_of_birth:
#         print("Неверно, введите дату в формате: 'dd.mm'")
#         day_of_birth = input("Введите день рождения А.С. Пушкина: ")
#         if day_of_birth == pushkin_day_of_birth:
#             print("Верно")
#
#
# def year():
#     year_of_birth = input("Введите год рождения А.С. Пушкина: ")
#     while year_of_birth != pushkin_year_of_birth:
#         print("Неверно, попробуйте ещё раз!")
#         year_of_birth = input("Введите год рождения А.С. Пушкина: ")
#     if year_of_birth == pushkin_year_of_birth:
#         day()
#
#
# year()
