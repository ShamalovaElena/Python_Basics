# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

name = input('Введите имя ')
surname = input('Введите фамилию ')
year = int(input('Введите год рождения '))
city = input('Введите место проживания ')
email = input('Введите email ')
telephone = input('Введите telephone ')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Шамалова', name = 'Елена', year = '1975', city = 'Москва', email = '12345@mail.ru', telephone = '89655657891'))



