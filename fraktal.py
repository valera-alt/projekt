from turtle import *

class Fraktal :


    def __init__(self, len = 10, width = 1, angle = 90):

        self.len = len
        self.width = width
        self.angle = angle

    def rules_fraktal(self,axiom, rule, iter = 1):

        for i in range(iter):
            axiom = axiom.lower()
            for j in rule:
                axiom = axiom.replace(j[0].lower(), j[1])

        self.axiom = axiom.upper()

        print(axiom)

    def set_turtle(self, x, y, a):
        penup()
        goto(x, y)
        setheading(a)
        pendown()

    def draw_fratal(self, x, y, a):
        screensize(5000,5000)
        tracer(10, 0)
        ht()
        pensize(self.width)
        penup()
        goto(x, y)
        setheading(a)
        pendown()
        turtle_stack = []

        print(self.axiom)
        for move in self.axiom:
            if move == 'F':
                fd(self.len)
            elif move == '+':
                left(self.angle)
            elif move == '-':
                left(-self.angle)
            elif move == 'S':
                penup()
                fd(self.len)
                pendown()
            elif move == '[':
                turtle_stack.append((xcor(), ycor(), heading(), pensize()))
            elif move == ']':
                x, y, a, w = turtle_stack.pop()
                self.set_turtle(x, y, a)
                self.width = w
                pensize(self.width)


        done()



a = Fraktal(4,1,90)
a.rules_fraktal('F-F-F-F',(("F", "F+S-FF+F+FF+FS+FF-S+FF-F-FF-FS-FFF"), ('S', 'SSSSSS')),3)


a.draw_fratal(0,200,0)













