# lesson_6-task_5
'''
Урок 6. Объектно-ориентированное программирование
Задача 5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''

class Stationary(): #

    def __init__(self, title):
        self.title = title
        print(f'Создан новый объект класса Stationary \n {self.title}\n')

    def Draw(self):
        print('Запуск отрисовки для базового класса\n')

class Pen(Stationary):
    def Draw(self):
        print('Запуск отрисовки для класса Pen\n')

class Pencil(Stationary):
    def Draw(self):
        print('Запуск отрисовки для класса Pencil\n')

class Handle(Stationary):
    def Draw(self):
        print('Запуск отрисовки для класса Handle\n')

new_stationary = Stationary('Здесь должен быть title для вызова базового класса')
new_stationary.Draw()

new_pen = Pen('Здесь должен быть title для вызова дочернего класса Pen')
new_pen.Draw()

new_pencil = Pencil('Здесь должен быть title для вызова дочернего класса Pencil')
new_pencil.Draw()

new_handle = Handle('Здесь должен быть title для вызова дочернего класса Handle')
new_handle.Draw()