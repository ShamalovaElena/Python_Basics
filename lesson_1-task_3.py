"""
# 3
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
"""
# 3
y = int(input("Введите число от 1 до 9 => "))
t = str(y)
t1 = t + t
t2 = t + t + t
total = y + int(t1) + int(t2)
print(total)