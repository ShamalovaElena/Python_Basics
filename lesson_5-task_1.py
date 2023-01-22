# lesson_5-task_1
'''
Урок 5. Работа с файлами
Задача 1. Создать (программный) файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка. '''

my_file = open('prog_file.txt', 'w')
line = input('Введите текст => \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст => \n')
    if not line:
        break
my_file.close()

my_file = open('prog_file.txt', 'r')
content = my_file.readlines()
# print(content)
print(f'Содержимое prog_file => , {content}')
my_file.close()