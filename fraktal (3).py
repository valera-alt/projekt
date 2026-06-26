from tkinter.ttk import Combobox
from turtle import *
from tkinter import *


class Fraktal:
    """
    Класс для генерации и отрисовки фракталов с использованием turtle graphics.
    """

    def __init__(self, len=5, width=1, angle=90):
        """
        Конструктор класса.

        Args:
            len (int): Длина шага черепахи.
            width (int): Толщина пера.
            angle (int): Угол поворота.
        """
        self.len = len
        self.width = width
        self.angle = angle

    def rules_fraktal(self, axiom, rule, iter=1):
        """
        Применяет правила замены к аксиоме для генерации строки фрактала.

        Args:
            axiom (str): Исходная строка (аксиома).
            rule (list): Список правил замены (кортежи).
            iter (int): Количество итераций.
        """
        for i in range(iter):
            axiom = axiom.lower()  # Переводим строку в нижний регистр
            for j in rule:
                # Заменяем символы согласно правилам
                axiom = axiom.replace(j[0].lower(), j[1])
        self.axiom = axiom.upper()  # Сохраняем строку в верхнем регистре
        print(self.axiom)  # Вывод строки для отладки

    def set_turtle(self, x, y, a):
        """
        Устанавливает положение и направление черепахи.

        Args:
            x (int): X-координата.
            y (int): Y-координата.
            a (int): Угол направления.
        """
        penup()  # Поднять перо
        goto(x, y)  # Перейти в координаты
        setheading(a)  # Повернуть черепаху
        pendown()  # Опустить перо

    def draw_fratal(self, x=0, y=0, a=90):
        """
        Отрисовывает фрактал по сгенерированной строке.

        Args:
            x (int): Начальная X-координата.
            y (int): Начальная Y-координата.
            a (int): Начальный угол направления.
        """
        screensize(5000, 5000)
        tracer(10, 0)  # Ускоряет рисование
        ht()  # Скрыть черепаху
        pensize(self.width)  # Установить толщину пера
        penup()
        goto(x, y)
        setheading(a)
        pendown()

        turtle_stack = []  # Стек для сохранения состояния черепахи

        print(self.axiom)  # Вывод строки для отладки

        for move in self.axiom:
            if move == 'F':
                fd(self.len)  # Движение вперед с рисованием
            elif move == '+':
                left(self.angle)  # Поворот налево
            elif move == '-':
                left(-self.angle)  # Поворот направо
            elif move == 'S':
                penup()
                fd(self.len)  # Движение вперед без рисования
                pendown()
            elif move == '[':
                # Сохранить текущее состояние черепахи
                turtle_stack.append((xcor(), ycor(), heading(), pensize()))
            elif move == ']':
                # Восстановить последнее сохранённое состояние
                x, y, a, w = turtle_stack.pop()
                self.set_turtle(x, y, a)
                self.width = w
                pensize(self.width)

        done()  # Завершить рисование


root = Tk()
root.geometry('400x310')
root.title("Рисование фракталов")


# Список подписей для полей ввода
labels_text = ['длинна шага:', 'толщина пера:', 'угол поворота:', 'X координата:',
               'Y координата:', 'направление:', 'аксиома:', 'правило:', 'итерации:']

# Создаем и размещаем подписи
for i, text in enumerate(labels_text):
    label = Label(root, text=text, font=5)
    label.grid(column=0, row=i)

# Список для хранения полей ввода
entries = []

# Создаем и размещаем поля ввода
for i in range(9):
    if i != 6:
        entry = Entry(root, font=5)
        entry.grid(column=1, row=i)
        entries.append(entry)
    else:
        continue

fraktal = ['СНЕЖИНКА КОХА', 'КРИВАЯ ЛЕВИ', 'ТРЕУГОЛЬНИК СЕРПИНСКОГО', 'КРИВАЯ ДРАКОНА', 'КРИВАЯ ГИЛЬБЕРТА', 'КУСТ', 'СОРНЯК', 'ДЕРЕВО ПИФАГОРА']
fraktal_axiom = ['F++F++F', 'F', 'FXF--FF--FF', 'FX', 'X', 'F', 'F', 'FX']
fraktal_rule = [[['F','F-F++F-F']], [['F', '-F+F']], [['F', 'FF'], ['X', '--FXF++FXF++FXF--']], [['FX', 'FX-FY'],['FY', 'FX+FY']],
[['X', '-YF+XFX+FY-'],['Y', '+XF-YFY-FX+']], [['F', 'FF+[+F-F-F]-[-F+F+F]']], [['F', 'F[+F]F[-F]F']], [['FX', 'FYFY[-FX][+FX]'],['FYFY', 'FYFYFY']]]
fraktal_gradus = ['60', '90', '60', '90', '90', '23', '26', '45']
axiom = Combobox(font = 5, width=18, values=fraktal)
axiom.grid(column=1, row=6)



def draw_fractal():
    """
    Функция для рисования фрактала на основе введенных данных.
    """



    entry_values = []
    for entry in entries:
        entry_values.append(entry.get())

    # Разбиваем строку с правилами на отдельные правила
    rules_str = entry_values[6].split(',')
    rules = []

    # Обрабатываем каждое правило и создаем список кортежей
    for rule in rules_str:
        rule_parts = rule.split('>')
        if len(rule_parts) == 2:
            rules.append((rule_parts[0], rule_parts[1]))

    ax = axiom.get()
    for i in range(len(fraktal)):
        if ax == fraktal[i]:
            ax = fraktal_axiom[i]
            rules = fraktal_rule[i]
            entry_values[2] = fraktal_gradus[i]
            entries[2].delete(0, END)
            entries[2].insert(END, fraktal_gradus[i])
            entries[6].delete(0, END)
            entries[6].insert(END, fraktal[i])
        else:
            continue


    # Создаем и настраиваем объект фрактала
    fractal = Fraktal(float(entry_values[0]), int(entry_values[1]), int(entry_values[2]))
    fractal.rules_fraktal(ax, rules, int(entry_values[7]))
    fractal.draw_fratal(int(entry_values[3]), int(entry_values[4]), int(entry_values[5]))


def clear_and_done():
    """
    Функция для очистки экрана и завершения рисования.
    """
    clear()
    done()


# Создаем кнопку для рисования фрактала
draw_button = Button(root, text='нарисовать', font=5, command=draw_fractal)
draw_button.grid(column=1, row=9)

# Создаем кнопку для очистки экрана
clear_button = Button(root, text='чистый лист', font=5, command=clear_and_done)
clear_button.grid(column=0, row=9)

root.mainloop()