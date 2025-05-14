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



    def draw_fratal(self, x, y):
        tracer(10, 0)
        ht()
        pensize(self.width)
        penup()
        goto(x, y)
        pendown()

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
        done()











k =[("F", "F+S-FF+F+FF+FS+FF-S+FF-F-FF-FS-FFF"),('S', 'SSSSSS')]
t = [('F','FX-FX--F++F++F-FX')]
dragon = [("FY", "-FX-FY"),('FX', 'FX+FY+')]
gilbert = [('X', '-YF+XFX+FY-'), ('Y', '+XF-YFY-FX+')]
triangle = [("F", "FF"), ("X", "++FXF--FXF--FXF++")]





b = Fraktal(1,1, 90)
b.rules_fraktal('FX', dragon, 16)
b.draw_fratal(00,00)
