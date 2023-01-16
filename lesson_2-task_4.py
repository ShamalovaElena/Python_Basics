#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
#Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
my_proposal = input("введите предложение ")
my_word = []
number = 1
for element in range(my_proposal.count(' ') + 1):
    my_word = my_proposal.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1