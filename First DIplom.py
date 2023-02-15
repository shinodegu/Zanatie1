import csv
import datetime
from datetime import datetime, time, date
from operator import itemgetter


with open('diplom.csv', 'r+', encoding='utf-8') as new_new_file:
    data_file = csv.reader(new_new_file)
    data = []
    for item in data_file:
        data.append(item)


def append_data():
    with open('diplom.csv', 'a', encoding='utf-8', newline='') as new_file:
        file_append = csv.writer(new_file)
        file_append.writerow(information)


information = []


def new_data():
    fio = input('Введите ФИО ')
    information.append(fio.title())

    birthday = input('Введите дату рождения через пробел: ')
    information.append(' Дата рождения: ' + birthday)

    date_of_death = input('Введите дату смерти, если человек жив введите 0 ')

    sex = input('Введите пол м/ж ')
    information.append(" " + sex)

    def calculator_live():
        born = datetime.strptime(birthday, '%d %m %Y')
        today = date.today()
        ages = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return information.append(f' Возраст: {str(ages)}')

    def death_calculator():
        born = datetime.strptime(birthday, '%d %m %Y')
        death = datetime.strptime(date_of_death, '%d %m %Y')
        ages = death.year - born.year - ((death.month, death.day) < (death.month, death.day))
        return information.append(f' Возраст: {str(ages)}'), information.append(" Дата смерти: " + date_of_death)

    while True:
        if date_of_death.isdigit():
            calculator_live()
        elif not date_of_death.isdigit():
            death_calculator()
        break


def found_info():
    name_person = input('Введите имя ')
    name_person = name_person.title()

    for search in data:
        if name_person in search[0]:
            print(search)
        elif len(search[0]) == 0:
            continue


while True:
    start_work = input("Добавить новые данные, введите Добавить"
                       "\nНайти данные о человеке, введите Поиск "
                       "\nВыйим из программы, введите Выход "
                       "\nЕсли хотите сохранить добавленные данные введите Сохранить"
                       "\n:")
    if start_work.upper() in "ДОБАВИТЬ":
        new_data()
    elif start_work.upper() in "СОХРАНИТЬ":
        append_data()
    elif start_work.upper() in "ПОИСК":
        found_info()
    elif start_work.upper() in "ВЫХОД":
        break
