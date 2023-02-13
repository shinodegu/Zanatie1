import csv
import datetime
from datetime import datetime, time, date
from operator import itemgetter
import re




with open('diplom.csv', 'r+', encoding='utf-8') as new_new_file:
    data_file = csv.reader(new_new_file)
    data = []
    for item in data_file:
        data.append(item)

print(data)

information = []

# def new_data():
#     fio = input('Введите ФИО ')
#     information.append(fio)
#
#     birthday = input('Введите дату рождения ')
#     information.append(' '+birthday)
#
#     date_of_death = input('Введите дату смерти, если человек жив введите 0 ')
#
#     sex = input('Введите пол м/ж ')
#     information.append(" " + sex)
#
#     def calculator_live():
#         born = datetime.strptime(birthday, '%d %m %Y')
#         today = date.today()
#         ages = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#         return information.append(' ' + ages), information.append(" Человек жив")
#
#     def death_calculator():
#         born = datetime.strptime(birthday, '%d %m %Y')
#         death = datetime.strptime(date_of_death, '%d %m %Y')
#         ages = death.year - born.year - ((death.month, death.day) < (death.month, death.day))
#         return information.append(ages), information.append(" Человек мертв " + date_of_death)
#
#     while True:
#         if date_of_death.isdigit():
#             calculator_live()
#         elif not date_of_death.isdigit():
#             death_calculator()
#         break


# new_data()

# print(information)
# print(data)

aboba = input('Введите имя ')
for index, list_of_numbers in enumerate(data):
    if aboba == list_of_numbers[0]:
      print('list[{0:d}][0]'.format(index))

# indecec = [index for (index, list_of_numbers) in enumerate(data) if list_of_numbers == aboba]
# for index in indecec:
#     asd = ('[{0:d}][0]'.format(index))
#     print(asd[])

# search = input("Введите имя поиска ")

# with open('diplom.csv') as file:
#     words = re.findall(
#         f'[\s\W]*(\w*{search}\w*)[\s\W]*', file.read(), re.IGNORECASE)
#
# print(words)

# result = [(n,x.index(search)) for n,x in enumerate(data) if search in x]
# print(result)

# search = input("Введите имя поиска ")
#
# filtering = list(filter(lambda x: search in x, data))
# print(filtering)

# indices = [i for i, x in enumerate(data) if x[0] == search]
# print(data[indices])
#
# print(any(search in inner_list for inner_list in data))

with open('diplom.csv', 'a', encoding='utf-8', newline='') as new_new_file:
    file_writer = csv.writer(new_new_file)
    # file_writer.writerow(information)
