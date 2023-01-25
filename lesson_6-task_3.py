# lesson_6-task_3
'''
Урок 6. Объектно-ориентированное программирование
Задача 3. Реализовать базовый класс Worker (работник). определить атрибуты: name, surname, position (должность),
income (доход); последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.

'''

class Worker(): # РАБОТНИК

    def __init__(self, lname, fname, position, wage, bonus):
        self.lname = lname
        self.fname = fname
        self.position = position

        # Здесь могу ошибаться, не до конца поняла суть задания про последний атрибут
        # Реализовал так: bonus задается в процентах от оклада, а в словарь записываю расчитанную сумму премии
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus':  self.wage * self.bonus / 100}

class Position(Worker):

    def get_full_name(self):
        return self.lname + ' ' + self.fname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

w1 = Position('Абрамов', 'Изя', 'парикмахер', 50000, 25)
print('Фамилия = ', w1.lname)
print('Имя = ', w1.fname)
print('Должность = ', w1.position)
print('Полное имя = ', w1.get_full_name())
print('Оклад, руб. = ', w1.wage)
print('Размер премии, % = ', w1.bonus)
print('Размер дохода, руб. = ', w1.get_total_income())
print(' --- ')

w2 = Position('Сахарова', 'Цецилия', 'Администратор салона', 67000, 20)
print('Фамилия = ' , w2.lname)
print('Имя = ', w2.fname)
print('Должность = ', w2.position)
print('Полное имя = ', w2.get_full_name())
print('Оклад, руб. = ', w2.wage)
print('Размер премии, % = ', w2.bonus)
print('Размер дохода, руб. = ', w2.get_total_income())
print(' --- ')