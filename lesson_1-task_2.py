"""
# 2
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
#2
x = int(input("Введите время в секундах => "))
sec = x % 3600
min = sec // 60
seconds = sec % 60
print("hour = ", hour)
print("minute = ", min)
print("seconds = ", seconds)
print(f"Время в формате ч:м:с - {sec / 3600:.2f} : {sec / 60:.2f} : {sec}")
