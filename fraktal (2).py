from turtle import *

class Fraktal:
    # Конструктор класса — инициализирует параметры фрактала
    # len — длина шага черепахи, width — толщина пера, angle — угол поворота
    def __init__(self, len=5, width=1, angle=90):
        self.len = len
        self.width = width
        self.angle = angle

    # Метод для применения правил замены к аксиоме (генерация строки фрактала)
    # axiom — исходная строка, rule — список правил замены (кортежи), iter — количество итераций
    def rules_fraktal(self, axiom, rule, iter=1):
        for i in range(iter):
            axiom = axiom.lower()  # переводим строку в нижний регистр для удобства замены
            for j in rule:
                # заменяем символы согласно правилам (j[0] — символ для замены, j[1] — на что заменяем)
                axiom = axiom.replace(j[0].lower(), j[1])
        self.axiom = axiom.upper()  # сохраняем итоговую строку в верхнем регистре для рисования
        print(axiom)  # вывод строки для отладки

    # Метод для установки положения и направления черепахи
    def set_turtle(self, x, y, a):
        penup()         # поднять перо, чтобы не рисовать при перемещении
        goto(x, y)      # перейти в координаты (x, y)
        setheading(a)   # повернуть черепаху в угол a (в градусах)
        pendown()       # опустить перо, чтобы начать рисовать

    # Метод для отрисовки фрактала по сгенерированной строке
    # x, y, a — начальные координаты и угол направления черепахи
    def draw_fratal(self, x=0, y=0, a=90):
        tracer(10, 0)       # ускоряет рисование, обновляя экран каждые 10 шагов
        ht()                # скрыть курсор черепахи (hide turtle)
        pensize(self.width) # установить толщину пера
        penup()
        goto(x, y)
        setheading(a)
        pendown()

        turtle_stack = []   # стек для сохранения состояния черепахи (позиция, угол, толщина пера)

        print(self.axiom)   # вывод строки для отладки

        for move in self.axiom:
            if move == 'F':
                fd(self.len)           # движение вперёд на длину шага с рисованием
            elif move == '+':
                left(self.angle)       # поворот налево на заданный угол
            elif move == '-':
                left(-self.angle)      # поворот направо (обратный поворот налево)
            elif move == 'S':
                penup()
                fd(self.len)           # движение вперёд без рисования
                pendown()
            elif move == '[':
                # сохранить текущее состояние черепахи в стек
                turtle_stack.append((xcor(), ycor(), heading(), pensize()))
            elif move == ']':
                # вернуться к последнему сохранённому состоянию
                x, y, a, w = turtle_stack.pop()
                self.set_turtle(x, y, a)
                self.width = w
                pensize(self.width)

        #done()  # завершить рисование и показать окно


axiom = ['F++F++F', 'FX', 'X', 'FXF--FF--FF', 'F++F++F++F', 'F', 'FX']
rule = [[['F', 'F-F++F-F']], [['FX','FX+FY+'],['FY','-FX-FY']], [['X', '-YF+XFX+FY-'],['Y', '+XF-YFY-FX+']], [['X' ,'--FXF++FXF++FXF--'],['F','FF']],
        [[ 'F' , '-F++F-']], [['F', 'F[+F]F[-F]F']], [['FX','FYFY[+FX]F[-FX]F'], ['FYFY','FYFYFY']]]
ugol = [60, 90, 90, 60, 45, 180/7, 45]
iter = [4, 12, 6, 6, 11, 4, 10]
ug = [0,0,0,180,0,90,90]

i = 6



a = Fraktal(1, 1, ugol[i])
a.rules_fraktal(axiom[i], rule[i], iter[i])
a.draw_fratal(0,0,ug[i])


done()


