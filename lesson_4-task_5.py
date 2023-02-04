# lesson_4-task_5

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce
primary_list = [x for x in range (100, 1001, 2)]
print(f'Формируем список четных от 100 до 1000 (включая границы) => {primary_list}')
rez = reduce(lambda item, item2: item*item2, primary_list)
print(f'Получаем результат произведения всех элементов полученного списка => {rez}')


