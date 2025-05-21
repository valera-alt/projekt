from tkinter import *

class Redaktor:
 root = Tk()
 root.title("валера word")
 root.geometry('10000x10000')
 root.configure(bg="#CCCCCC")

 scale = Scale(length=780, showvalue=0, sliderlength=200)

 scale.pack(anchor = E)


 y = 300
 txt = Text(width=180, height=500).place(x=40, y=y)




 def dvij(self):
     a = self.scale.get()
     return a


 scale.bind('<Motion>', dvij)



 root.mainloop()



sas = Redaktor()

sas.dvij()