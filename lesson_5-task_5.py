# lesson_5-task_5
'''
Урок 5. Работа с файлами
Задача 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

def rewrite_file():
    try:
        with open('numbers.txt', 'w+') as file:
            file.write(input('Введите числа через пробел => '))
            l = map(int, file.read().split())
            print(f'Сумма чисел numbers.txt => , {sum(l)}')
            # my_file.close()
    except FileNotFoundError:
        return 'Файл не найден.'

rewrite_file()

my_file = open('numbers.txt', 'r')
content = my_file.readlines()
print(f'Содержимое numbers.txt => , {content}')
my_file.close()