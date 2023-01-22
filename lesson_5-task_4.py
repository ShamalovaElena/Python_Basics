# lesson_5-task_4
'''
Урок 5. Работа с файлами
Задача 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1 Two — 2 Three — 3 Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

def rewrite_file_en_ru():
    num = {'One' 'Один', 'Two' 'Два', 'Three' 'Три', 'Four' 'Четыре'}
    new_text = []
    try:
        with open('file_en.txt', 'r+', encoding="utf-8") as file:
            with open('file_ru.txt', 'r+', encoding="utf-8") as new_file:
                l = file.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                    new_file.writelines(new_text)
    except FileNotFoundError:
        return

rewrite_file_en_ru()

my_file = open('file_en.txt', 'r')
content = my_file.readlines()
print(f'Содержимое file_en.txt => , {content}')
my_file.close()

my_file = open('file_ru.txt', 'r')
content = my_file.readlines()
# print(content)
print(f'Содержимое file_ru.txt => , {content}')
my_file.close()